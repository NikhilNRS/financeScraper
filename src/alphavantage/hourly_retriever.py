import os
import requests
import time
import logging
import argparse
from datetime import datetime, timedelta
import pandas as pd
from io import StringIO

# Setup argument parser and logging
parser = argparse.ArgumentParser(description='Fetch financial data with verbose logging option.')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the .data directory exists
data_dir = '.data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

API_KEY = 'your-api-key'

def manage_rate_limit(request_counter, start_time):
    if request_counter % 30 == 0:
        elapsed_time = time.time() - start_time
        if elapsed_time < 60:
            sleep_time = 60 - elapsed_time
            logging.info(f"Approaching rate limit, pausing for {sleep_time} seconds.")
            time.sleep(sleep_time)
        return time.time()  # Reset start time
    return start_time

def fetch_and_append_data(symbol, start_year, end_year):
    request_counter = 0
    start_time = time.time()
    total_months = (end_year - start_year + 1) * 12
    logging.info(f"Fetching {total_months} months of hourly data for {symbol}.")

    data_frames = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            slice_month = f"{year}-{str(month).zfill(2)}"
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=60min&month={slice_month}&outputsize=full&apikey={API_KEY}&datatype=csv"
            response = requests.get(url)
            request_counter += 1
            logging.info(f"Request #{request_counter} for {symbol}: {slice_month}")
            
            if response.status_code == 200:
                csv_data = StringIO(response.content.decode('utf-8'))
                df = pd.read_csv(csv_data)
                data_frames.append(df)
            else:
                logging.error(f"Failed to fetch {symbol} for {slice_month}, HTTP Status: {response.status_code}")
            
            start_time = manage_rate_limit(request_counter, start_time)

    full_data = pd.concat(data_frames, ignore_index=True)
    filename = os.path.join(data_dir, f"{symbol}_hourly_data_{start_year}_to_{end_year}.csv")
    full_data.to_csv(filename, index=False)
    logging.info(f"Data saved to {filename}")

if __name__ == "__main__":
    symbols = ['BTC', 'ETH']  # Adjust symbols as needed
    for symbol in symbols:
        fetch_and_append_data(symbol, 2013, 2023)  # Example: Fetch 10 years of data

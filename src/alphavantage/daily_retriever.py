import os
import requests
import time
import logging
import argparse
from datetime import datetime
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

def fetch_daily_data(symbol):
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(data_dir, f"{symbol}_daily_data_{current_datetime}.csv")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}&datatype=csv"
    logging.info(f"Fetching daily data for {symbol}.")
    response = requests.get(url)
    
    if response.status_code == 200:
        csv_data = StringIO(response.content.decode('utf-8'))
        df = pd.read_csv(csv_data)
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename}")
    else:
        logging.error(f"Failed to fetch {symbol}, HTTP Status: {response.status_code}")

if __name__ == "__main__":
    symbols = ['BTC']  # Adjust symbols as needed
    for symbol in symbols:
        fetch_daily_data(symbol)
        manage_rate_limit(1, time.time())  # Assuming each symbol fetch counts as one request

import datetime
import os
import requests
import pandas as pd
import time
import logging
import argparse
import io

# Setup argument parser
parser = argparse.ArgumentParser(description='Fetch economic data with optional verbose logging.')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

API_KEY = 'your-api-key'  # Your premium API key
BASE_URL = 'https://www.alphavantage.co/query'
DATA_DIR = '.eco_data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def manage_rate_limit(current_request_count):
    if current_request_count % 30 == 0:
        if args.verbose:
            logging.info("Approaching rate limit, pausing for 60 seconds.")
        time.sleep(60)

def fetch_data(function, interval='annual'):
    params = {
        'function': function,
        'interval': interval,
        'apikey': API_KEY,
        'datatype': 'csv',
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        csv_string = response.content.decode('utf-8')
        csv_file = io.StringIO(csv_string)  # Convert string to a file-like object
        df = pd.read_csv(csv_file)  # Now you can read it with pd.read_csv
        return df
    else:
        if args.verbose:
            logging.error(f"Failed to fetch data for {function}. HTTP Status: {response.status_code}")
        return pd.DataFrame()
    
def save_data(df, filename):
    filepath = os.path.join(DATA_DIR, filename)
    df.to_csv(filepath, index=False)
    if args.verbose:
        logging.info(f"Data saved to {filepath}")

def main():
    indicators = [
        'REAL_GDP', 'REAL_GDP_PER_CAPITA', 'TREASURY_YIELD', 
        'FEDERAL_FUNDS_RATE', 'CPI', 'INFLATION', 
        'RETAIL_SALES', 'DURABLES', 'UNEMPLOYMENT', 'NONFARM_PAYROLL'
    ]
    request_count = 0
    for indicator in indicators:
        if args.verbose:
            logging.info(f"Fetching data for {indicator}")
        df = fetch_data(indicator)
        request_count += 1
        if not df.empty:
            today = datetime.datetime.now().strftime('%Y-%m-%d')  # Corrected usage
            filename = f"{indicator.lower()}_{today}.csv"
            save_data(df, filename)
        manage_rate_limit(request_count)
        time.sleep(2)  # Additional sleep to ensure we don't hit the rate limit

if __name__ == "__main__":
    main()

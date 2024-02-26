import json
import requests
import pandas as pd
import os
import logging
from datetime import datetime

# Initialize logging
LOGS_DIR = './logs'
os.makedirs(LOGS_DIR, exist_ok=True)
logging.basicConfig(filename=f'{LOGS_DIR}/data_collection.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = 'your-api-key'
BASE_URL = 'https://www.alphavantage.co/query?'
OUTPUT_FOLDER = './data'

# Ensure output directory exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def save_response(data, function):
    """Saves a sample API response for debugging."""
    filename = f'sample_{function.lower()}_response.json'
    filepath = os.path.join(LOGS_DIR, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    logging.info(f"Sample response for {function} saved to {filepath}")

def fetch_data(symbol, market, function):
    logging.info(f"Fetching {function} data for {symbol}")
    params = {
        'function': function,
        'symbol': symbol,
        'market': market,
        'apikey': API_KEY,
        'datatype': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        logging.info(f"Data fetched successfully for {function}")
        data = response.json()
        save_response(data, function)  # Save a sample response
        return data
    else:
        logging.error(f"Failed to fetch data: {response.status_code}")
        return None

def process_and_save_data(data, symbol, function_info):
    function, interval = function_info if isinstance(function_info, tuple) else (function_info, None)
    if data is None:
        logging.error("No data to process")
        return
    # Adjust the key based on function to access data correctly
    if 'intraday' in function.lower():
        key = 'Time Series (Digital Currency Intraday)'
    else:
        key = next(k for k in data if 'Time Series' in k)
    df = pd.DataFrame(data[key]).T
    interval_suffix = interval if interval else function.split('_')[-1].lower()  # Use interval or extract from function
    filename = f"{symbol}_{interval_suffix}.csv"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    df.to_csv(filepath)
    logging.info(f"Data saved to {filepath}")

# In the main execution block, when calling process_and_save_data, ensure function information is passed correctly.
if __name__ == "__main__":
    intervals_functions = {
        'hourly': ('CRYPTO_INTRADAY', '60min'),  # Assuming 'hourly' requires specifying '60min'
        'daily': 'DIGITAL_CURRENCY_DAILY',
        'weekly': 'DIGITAL_CURRENCY_WEEKLY',
        'monthly': 'DIGITAL_CURRENCY_MONTHLY'
    }

    symbol = 'BTC'
    market = 'USD'
    for interval, function in intervals_functions.items():
        # For hourly data, we need to adjust the API parameters to include 'interval'
        if interval == 'hourly':
            data = fetch_data(symbol, market, function[0])  # Passing function only, interval handled internally
        else:
            data = fetch_data(symbol, market, function)
        process_and_save_data(data, symbol, function)

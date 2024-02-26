import requests
import json
import logging
import os

# Directories for data and logs
LOGS_DIR = './logs'
DATA_DIR = './data'
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Setup logging to save in logs directory
log_file_path = os.path.join(LOGS_DIR, 'crypto_intraday_fetch.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = 'your-api-key'
BASE_URL = 'https://www.alphavantage.co/query?'

def fetch_crypto_intraday(symbol, market, interval):
    params = {
        'function': 'CRYPTO_INTRADAY',
        'symbol': symbol,
        'market': market,
        'interval': interval,
        'apikey': API_KEY,
        'datatype': 'csv',
        'outputsize': 'full'  # Request full data
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        logging.info("Successfully fetched full intraday data")
        return response.text
    else:
        logging.error(f"Failed to fetch data: {response.status_code}, {response.text}")
        return None


def save_data(data, filename):
    if data:
        file_path = os.path.join(DATA_DIR, filename)
        with open(file_path, 'w') as file:
            file.write(data)  # Save CSV data directly
        logging.info(f"Data saved to {file_path}")
    else:
        logging.error("No data to save")

if __name__ == "__main__":
    symbol = 'BTC'
    market = 'USD'
    interval = '60min'
    data = fetch_crypto_intraday(symbol, market, interval)
    if data:
        filename = f"{symbol}_{interval}_intraday.csv"  # Change extension to .csv
        save_data(data, filename)
    else:
        logging.error("No data retrieved.")

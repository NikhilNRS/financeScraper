import datetime
import json
import os
import requests
import logging
import argparse

# Setup logging to both console and file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("sentiment_fetch_log.txt"),
                              logging.StreamHandler()])

# Setup argument parser
parser = argparse.ArgumentParser(description='Fetch sentiment data for a specific range of years.')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
parser.add_argument('-y', '--year', type=int, help='End year for fetching sentiment data', required=True)
args = parser.parse_args()

# Set logging level based on verbose flag
if args.verbose:
    logging.getLogger().setLevel(logging.INFO)

API_KEY = 'your-api-key'  # Replace with your actual API key
BASE_URL = 'https://www.alphavantage.co/query'
DATA_DIR = './sentiment_data'

# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def fetch_sentiment_data(ticker, year):
    start_date = f"{year}0101T0000"
    end_date = f"{year}1231T2359"
    params = {
        'function': 'NEWS_SENTIMENT',
        'tickers': ticker,
        'time_from': start_date,
        'time_to': end_date,
        'sort': 'LATEST',
        'limit': 1000,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    response_data = response.json() if response.status_code == 200 else {}
    
    # Instead of appending to a text file, directly save the JSON response
    if response_data:
        filename = f"response_{ticker}_{year}.json"
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w') as file:
            json.dump(response_data, file)
        logging.info(f"Response data saved for {ticker} in {year} to {filepath}")
    else:
        logging.warning(f"No data available or failed request for {ticker} in {year}.")
    
    return response_data


def save_sentiment_data(data, filename):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file)
    logging.info(f"All data saved to {filepath}")

def main():
    tickers = ['CRYPTO:BTC', 'blockchain']
    end_year = args.year  # Get the end year from the command line argument
    all_data = {}

    for year in range(end_year - 9, end_year + 1):  # Last 10 years, inclusive of the end year
        for ticker in tickers:
            logging.info(f"Fetching sentiment data for {ticker} for the year {year}")
            data = fetch_sentiment_data(ticker, year)
            if not all_data.get(ticker):
                all_data[ticker] = []
            all_data[ticker].extend(data.get('items', []))  # Assuming 'items' contains the articles

    save_sentiment_data(all_data, f"sentiment_data_{end_year-9}_to_{end_year}.json")

if __name__ == "__main__":
    main()

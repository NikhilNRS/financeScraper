import requests
import csv
import os
import argparse

# Parse command line arguments for verbosity
parser = argparse.ArgumentParser(description='Fetch NYSE and LSE ticker symbols with MarketStack API.')
parser.add_argument('-v', '--verbose', action='count', default=0, help='Increase output verbosity (up to -vv for more detailed logs)')
args = parser.parse_args()

def fetch_symbols_page(api_key, url, exchange, all_symbols, request_counter, verbose):
    if request_counter['count'] >= 10000:
        if verbose:
            print("Request limit reached. Stopping further requests.")
        return

    while True:
        params = {
            'access_key': api_key,
            'exchange': exchange,
            'limit': 100,
            'offset': request_counter['count'] * 100
        }
        response = requests.get(url, params=params)
        request_counter['count'] += 1

        if verbose > 1:  # Detailed logging for -vv option
            print(f"Request {request_counter['count']}: Fetching symbols for {exchange}... Response Status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            all_symbols.extend(data.get('data', []))

            if verbose > 1:  # Log pagination details for -vv option
                print(f"Pagination details: {data.get('pagination')}")

            # Check if we've fetched all available symbols based on pagination total
            if len(all_symbols) >= data['pagination']['total']:
                break
        else:
            print(f"Failed to fetch symbols for {exchange}: {response.status_code}")
            break


def list_symbols_for_exchanges(api_key, exchanges, verbose):
    """Fetch available symbols from the MarketStack API for specified exchanges and handle pagination with a request limit."""
    base_url = "http://api.marketstack.com/v1/tickers"
    
    for exchange in exchanges:
        all_symbols = []
        request_counter = {'count': 0}

        fetch_symbols_page(api_key, base_url, exchange, all_symbols, request_counter, verbose)
        
        # Ensure the .data folder exists
        data_folder = '.data'
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        
        # Define the filename and path
        filename = f'{exchange}_symbols.csv'
        filepath = os.path.join(data_folder, filename)
        
        # Open the CSV file and write the data
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Symbol', 'Name'])  # Header row
            for symbol in all_symbols:
                writer.writerow([symbol['symbol'], symbol['name']])
                
        if verbose > 0:  # Log summary information at any verbosity level (-v or -vv)
            print(f"Symbols for {exchange} have been saved to {filepath}. Requests made: {request_counter['count']}")

api_key = 'your-api-key'
exchanges = ['XNYS', 'XLON']  # Assuming 'XNYS' is NYSE and 'XLON' is LSE; adjust as necessary based on actual API identifiers
list_symbols_for_exchanges(api_key, exchanges, args.verbose)

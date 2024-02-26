import requests
import csv
from datetime import datetime, timedelta
import os
import argparse

# Parse command line arguments for verbosity
parser = argparse.ArgumentParser(description='Fetch financial data with MarketStack API.')
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='Increase output verbosity (-v for request count, -vv for detailed response logging)')
args = parser.parse_args()

def fetch_financial_data(api_key, symbol, date_from, date_to, interval, request_limit):
    """Fetch financial data for a given symbol and interval, respecting a request limit."""
    base_url = "http://api.marketstack.com/v1/eod" if interval == "daily" else "http://api.marketstack.com/v1/intraday"
    params = {
        'access_key': api_key,
        'symbols': symbol,
        'date_from': date_from,
        'date_to': date_to,
        'offset': 0
    }
    if interval != "daily":
        params['interval'] = interval

    data_collected = []
    request_count = 0
    total_expected_entries = None

    while request_count < request_limit:
        response = requests.get(base_url, params=params)
        request_count += 1

        if args.verbose > 0:
            print(f"Req {request_count}: {symbol}, Interval: {interval}")

        if response.status_code == 200:
            data = response.json()
            entries_fetched = len(data['data'])
            data_collected.extend(data['data'])

            if total_expected_entries is None:
                total_expected_entries = data['pagination']['total']

            if args.verbose > 1:
                print(f"Req {request_count} Status: {response.status_code}, Fetched: {entries_fetched}, Offset: {params['offset']}")

            params['offset'] += entries_fetched
            if entries_fetched == 0 or params['offset'] >= total_expected_entries:
                break
        else:
            print(f"Fetch Error: {response.status_code}")
            break

    print(f"Total Requests: {request_count}, Total Entries Fetched: {len(data_collected)} of {total_expected_entries} for {symbol}.")
    return data_collected

# Ensure the .data folder exists
data_folder = '.data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Define the date range for the last 10 years
date_to = datetime.now()
date_from = date_to - timedelta(days=365 * 10)

# Adjusted symbols with correct tickers
symbols = {'GOLD': 'PHAU.XLON'}
intervals = ['daily']

for name, symbol in symbols.items():
    for interval in intervals:
        data = fetch_financial_data('your-api-key', symbol, date_from.strftime('%Y-%m-%d'), date_to.strftime('%Y-%m-%d'), interval, 100)
        if data:
            filename = os.path.join(data_folder, f"{name.lower().replace(' ', '_')}_data_{interval}.csv")
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Closing Price'])
                for item in data:
                    date = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S%z').date()
                    closing_price = item['close']
                    writer.writerow([date, closing_price])
            print(f"Data for {symbol} at {interval} interval has been saved to {filename}.")
        else:
            print(f"No data was fetched for {symbol} at {interval} interval.")

print("Data fetching and saving complete.")

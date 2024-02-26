import requests
import csv
import os

def fetch_and_save_tickers(api_key, filepath, request_limit):
    """Fetch tickers with pagination and save them to a CSV file, respecting a request limit."""
    base_url = "http://api.marketstack.com/v1/tickers"
    params = {
        'access_key': api_key,
        'exchange': 'INDX',
        'limit': 100,  # Maximum entries per request as per API documentation
        'offset': 0  # Start at the beginning
    }
    
    request_count = 0  # Initialize request counter
    total_entries = 0  # Track the total number of entries fetched

    while request_count < request_limit:
        response = requests.get(base_url, params=params)
        request_count += 1  # Increment request counter for each API call

        if response.status_code == 200:
            data = response.json()
            total_entries += len(data.get('data', []))
            with open(filepath, mode='a', newline='') as file:  # Append mode
                writer = csv.writer(file)
                for ticker in data.get('data', []):
                    writer.writerow([
                        ticker.get('symbol'),
                        ticker.get('name'),
                        ticker.get('exchange')
                    ])
            # Update offset for the next request
            params['offset'] += params['limit']

            # Break if all entries have been fetched
            if total_entries >= data['pagination']['total']:
                break
        else:
            print(f"Failed to fetch tickers: {response.status_code}")
            break

    print(f"Completed {request_count} requests, fetched {total_entries} entries. Data saved to {filepath}.")

def list_tickers_for_indx_with_pagination_and_limit(api_key, request_limit=50):
    """Fetch all tickers associated with 'INDX' exchange, handling pagination and respecting a request limit."""
    data_folder = '.data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    filename = 'tickers_for_indx_with_pagination_and_limit.csv'
    filepath = os.path.join(data_folder, filename)
    
    # Create or clear the file before appending data
    open(filepath, 'w').close()
    
    # Write headers
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Ticker', 'Name', 'Exchange'])
    
    fetch_and_save_tickers(api_key, filepath, request_limit)

api_key = 'your-api-key'
list_tickers_for_indx_with_pagination_and_limit(api_key)

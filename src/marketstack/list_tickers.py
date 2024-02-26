import requests
import csv
import os

def fetch_symbols_page(api_key, url, all_symbols, request_counter):
    """Fetch a page of symbols, return the next page URL, if any, and update the request counter."""
    if request_counter['count'] >= 10000:
        print("Request limit reached. Stopping further requests.")
        return None

    response = requests.get(url, params={'access_key': api_key})
    request_counter['count'] += 1  # Update the request counter for each API call

    if response.status_code == 200:
        data = response.json()
        all_symbols.extend(data.get('data', []))  # Extend the list with the symbols from the current page
        # Check for a 'next' page link; adjust based on actual API response structure
        next_page_url = data.get('pagination', {}).get('next_page_url')
        return next_page_url
    else:
        print(f"Failed to fetch symbols: {response.status_code}")
        return None

def list_available_symbols_and_save(api_key):
    """Fetch available symbols from the MarketStack API and handle pagination with a request limit."""
    base_url = "http://api.marketstack.com/v1/tickers"
    all_symbols = []
    request_counter = {'count': 0}  # Initialize a request counter

    next_page_url = fetch_symbols_page(api_key, base_url, all_symbols, request_counter)
    
    # Handle pagination if next_page_url is provided and limit not reached
    while next_page_url and request_counter['count'] < 10000:
        next_page_url = fetch_symbols_page(api_key, next_page_url, all_symbols, request_counter)
        
    # Ensure the .data folder exists
    data_folder = '.data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    
    # Define the filename and path
    filename = 'available_symbols.csv'
    filepath = os.path.join(data_folder, filename)
    
    # Open the CSV file and write the data
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Symbol', 'Name'])  # Header row
        for symbol in all_symbols:
            writer.writerow([symbol['symbol'], symbol['name']])
            
    print(f"Available symbols have been saved to {filepath}. Requests made: {request_counter['count']}")

api_key = ' your-api-key'
list_available_symbols_and_save(api_key)

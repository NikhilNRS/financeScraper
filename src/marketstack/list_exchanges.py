import requests
import csv
import os

def list_available_exchanges_and_save(api_key):
    """Fetch available exchanges from the MarketStack API and save them to a CSV file."""
    base_url = "http://api.marketstack.com/v1/exchanges"  # Endpoint for exchanges
    params = {
        'access_key': api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        exchanges_data = response.json()
        
        # Ensure the .data folder exists
        data_folder = '.data'
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        
        # Define the filename and path
        filename = 'available_exchanges.csv'
        filepath = os.path.join(data_folder, filename)
        
        # Open the CSV file and write the data
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Exchange Code', 'Name', 'Region', 'Country'])  # Header row
            
            for exchange in exchanges_data.get('data', []):
                writer.writerow([
                    exchange.get('mic'),  # Market Identifier Code (MIC)
                    exchange.get('name'),
                    exchange.get('region'),
                    exchange.get('country')
                ])
                
        print(f"Available exchanges have been saved to {filepath}.")
    else:
        print(f"Failed to fetch exchanges: {response.status_code}")

api_key = 'your-api-key'
list_available_exchanges_and_save(api_key)

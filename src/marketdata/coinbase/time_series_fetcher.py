import sys
import json
from datetime import datetime, timedelta

# Add the path to the local Historic_Crypto library before importing it
sys.path.insert(0, '/Users/nikhilrazab-sekh/Desktop/Personal_Projects/CryptoData/data_extraction/lib')


# Now you can import your local version of Historic_Crypto
from Historic_Crypto import HistoricalData

# Your existing code follows


# Calculate date 5 years ago from today, include dummy time
start_date = (datetime.now() - timedelta(days=10*365)).strftime('%Y-%m-%d-00-00')
# Today's date as the end date, include dummy time
end_date = datetime.now().strftime('%Y-%m-%d-23-59')

# The granularity for the data in seconds (3600 seconds = 1 hour)
granularity = 3600

# Retrieve historical data for BTC-USD for the last 5 years, hourly
try:
    data = HistoricalData('BTC-USD', granularity, start_date, end_date).retrieve_data()
    
    # Convert the data to a list of dictionaries for JSON serialization
    data_list = []
    for timestamp, row in data.iterrows():
        data_dict = {
            "time": str(timestamp),
            "low": row['low'],
            "high": row['high'],
            "open": row['open'],
            "close": row['close'],
            "volume": row['volume']
        }
        data_list.append(data_dict)
    
    # Specify the output JSON file path
    json_file_path = 'btc_data_15_yrs_hourly.json'
    
    # Serialize the data to JSON and save it to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)
        
    print(f"Data saved to {json_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

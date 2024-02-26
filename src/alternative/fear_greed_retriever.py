import requests
import csv
from datetime import datetime
import os

# Ensure the .data directory exists
data_dir = ".data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Endpoint from the Alternative.me API documentation
api_url = "https://api.alternative.me/fng/?limit=0"

# Counter for the number of requests made
request_count = 0

try:
    # Make the GET request
    response = requests.get(api_url)
    request_count += 1  # Increment request count
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Specify the path to the CSV file within the .data directory
        csv_file_path = os.path.join(data_dir, 'fear_and_greed_index.csv')
        
        # Open a CSV file to write the data
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Value", "Classification"])
            
            # Loop through the data items and write to CSV
            for item in data['data']:
                # Convert timestamp to readable format
                timestamp = datetime.fromtimestamp(int(item['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([timestamp, item['value'], item['value_classification']])
        
        print(f"Data written to CSV in .data folder. Number of requests made: {request_count}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

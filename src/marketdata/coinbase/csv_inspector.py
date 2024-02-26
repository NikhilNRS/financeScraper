import csv
import os

def inspect_csv_file(file_path):
    try:
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            # Load all rows into a list (consider memory for very large files)
            rows = list(reader)
            print(f"Loaded {file_path} successfully.")
            
            # Step 1: Count the number of rows (excluding header)
            print(f"Total rows in file (excluding header): {len(rows) - 1}")
            
            # Step 2: Inspect the first row (header) and the second row (first data row)
            if len(rows) > 0:
                print("Column names (header):")
                print(rows[0])  # Print header
            if len(rows) > 1:
                print("First row of data:")
                print(rows[1])  # Print first data row
                
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    # Step 3: Inspect the file size
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes")

# Replace 'btc_data_15_yrs_hourly.csv' with your actual CSV file path if different
file_path = '../data/btc_data_15_yrs_6hrs.csv'
inspect_csv_file(file_path)

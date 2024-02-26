import json
import os
import csv

def inspect_json_file(file_path):
    # Step 1: Read the JSON file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"Loaded {file_path} successfully.")
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return

    # Step 2: Inspect the size and number of objects
    if isinstance(data, list):
        print(f"Total objects in file: {len(data)}")
    elif isinstance(data, dict):
        print("The JSON structure is a dictionary. The count applies to its keys.")
        print(f"Total keys in the dictionary: {len(data)}")
    else:
        print("The JSON structure is neither a list nor a dictionary.")

    # Step 3: Inspect the first object (if the data is a list)
    if isinstance(data, list) and len(data) > 0:
        print("Inspecting the first object:")
        print(json.dumps(data[0], indent=4))
    elif isinstance(data, dict):
        print("Inspecting the dictionary (showing keys):")
        print(list(data.keys()))

    # Step 4: Inspect the file size
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes")

    # Step 5: Print keys (if applicable)
    if isinstance(data, list) and len(data) > 0:
        keys = data[0].keys()
        print(f"Keys in each object: {keys}")
    elif isinstance(data, dict):
        print(f"Keys in the dictionary: {list(data.keys())}")

    # Step 6: Convert JSON to CSV
    csv_file_path = file_path.replace('.json', '.csv')
    convert_json_to_csv(data, csv_file_path)

def convert_json_to_csv(json_data, csv_file_path):
    # Assuming json_data is a list of dictionaries
    if not json_data or not isinstance(json_data, list):
        print("No data to convert or incorrect format.")
        return
    
    keys = json_data[0].keys()
    with open(csv_file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(json_data)
    print(f"CSV file created successfully at {csv_file_path}")

# File path adjusted to target the specified JSON file
file_path = 'btc_data_15_yrs_6hrs.json'
inspect_json_file(file_path)

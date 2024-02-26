import pandas as pd

# Replace 'your_file.csv' with the path to your actual CSV file
file_path = '/Users/nikhilrazab-sekh/Desktop/Personal_Projects/CryptoData/data_extraction/.data/btc_data_15_yrs_daily.csv'

def load_and_describe_csv(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Basic info about the DataFrame
    print("Basic Information about the CSV file:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("Column names:", df.columns.tolist())
    
    # Display basic statistics for numerical columns
    print("\nBasic Statistics for Numerical Columns:")
    print(df.describe())
    
    # Display the first 5 rows of the DataFrame
    print("\nSample Data (First 5 Rows):")
    print(df.head())

# Call the function with your file path
load_and_describe_csv(file_path)

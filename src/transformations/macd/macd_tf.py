import pandas as pd
import os

# Input file path
input_file_path = '/Users/nikhilrazab-sekh/Desktop/CryptoData/data_extraction/src/transformations/.transformed_data/btc_data_15_yrs_hourly.csv'

# Output directory path, adjusted to be one level higher
output_dir = os.path.join('..', '.transformed_data')

# Ensure the output directory exists, create if it does not
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate the output file path by joining the output directory with the input file name
output_file_path = os.path.join(output_dir, os.path.basename(input_file_path))

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Ensure 'time' is the index and in datetime format (if not already)
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)

# Check for MACD column and calculate if necessary
if 'MACD' not in df.columns:
    # MACD = 12-period EMA - 26-period EMA
    ema_12 = df['close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26

# Save the updated DataFrame to the new output file path
df.to_csv(output_file_path)

print(f"MACD calculation completed and added to the CSV. Output file saved to: {output_file_path}")
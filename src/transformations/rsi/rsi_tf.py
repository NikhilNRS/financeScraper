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
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)

# Calculate RSI
delta = df['close'].diff(1)
gain = (delta.where(delta > 0, 0)).ewm(span=14, adjust=False).mean()
loss = (-delta.where(delta < 0, 0)).ewm(span=14, adjust=False).mean()
rs = gain / loss
df['RSI'] = 100 - (100 / (1 + rs))

# Save the updated DataFrame to the new output file path
df.to_csv(output_file_path)

print(f"RSI calculation completed and added to the CSV. Output file saved to: {output_file_path}")

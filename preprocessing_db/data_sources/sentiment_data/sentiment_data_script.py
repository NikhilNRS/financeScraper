import pandas as pd

# Generated Python script
file_path_1 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/sentiment_data/response_CRYPTO:BTC_2022.csv'
file_path_2 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/sentiment_data/response_CRYPTO:BTC_2023.csv'
file_path_3 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/sentiment_data/fear_and_greed_index.csv'

# List containing all file path variables
all_files = [file_path_1, file_path_2, file_path_3]

# Loading files into DataFrames and printing the first 5 rows
df1 = pd.read_csv(file_path_1)
print(f'\nDataFrame 1 - First 5 Rows:')
print(df1.head())

df2 = pd.read_csv(file_path_2)
print(f'\nDataFrame 2 - First 5 Rows:')
print(df2.head())

df3 = pd.read_csv(file_path_3)
print(f'\nDataFrame 3 - First 5 Rows:')
print(df3.head())


import pandas as pd

# Generated Python script
file_path_1 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/DIA_daily_data_20240226_003856.csv'
file_path_2 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/SPY_hourly_data_2013_to_2023.csv'
file_path_3 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/SPY_daily_data_20240226_003855.csv'
file_path_4 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/GLD_hourly_data_2013_to_2023.csv'
file_path_5 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/DIA_hourly_data_2013_to_2023.csv'
file_path_6 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/GOLD_hourly_data_2013_to_2023.csv'
file_path_7 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/GLD_daily_data_20240226_003855.csv'
file_path_8 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/inxdata_alpha_vantage/GOLD_daily_data_20240226_093424.csv'

# List containing all file path variables
all_files = [file_path_1, file_path_2, file_path_3, file_path_4, file_path_5, file_path_6, file_path_7, file_path_8]

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

df4 = pd.read_csv(file_path_4)
print(f'\nDataFrame 4 - First 5 Rows:')
print(df4.head())

df5 = pd.read_csv(file_path_5)
print(f'\nDataFrame 5 - First 5 Rows:')
print(df5.head())

df6 = pd.read_csv(file_path_6)
print(f'\nDataFrame 6 - First 5 Rows:')
print(df6.head())

df7 = pd.read_csv(file_path_7)
print(f'\nDataFrame 7 - First 5 Rows:')
print(df7.head())

df8 = pd.read_csv(file_path_8)
print(f'\nDataFrame 8 - First 5 Rows:')
print(df8.head())


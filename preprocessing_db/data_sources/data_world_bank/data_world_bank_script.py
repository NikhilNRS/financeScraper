import pandas as pd

# Generated Python script
file_path_1 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/inflation_rates_usa.csv'
file_path_2 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/trade_balance_usa.csv'
file_path_3 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/world_bank_economic_indicators_nl.csv'
file_path_4 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/central_bank_policy_rates_usa.csv'
file_path_5 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/world_bank_indicators.csv'
file_path_6 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/mobile_cellular_subscriptions_usa.csv'
file_path_7 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/foreign_direct_investment_usa.csv'
file_path_8 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/stock_market_indices_usa.csv'
file_path_9 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/internet_penetration_usa.csv'
file_path_10 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/world_bank_economic_indicators.csv'
file_path_11 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/total_public_debt_gdp_usa.csv'
file_path_12 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/world_bank_economic_indicators_usa.csv'
file_path_13 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/gdp_growth_rates_usa.csv'
file_path_14 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/domestic_credit_private_sector_usa.csv'
file_path_15 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/unemployment_rates_usa.csv'
file_path_16 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/remittances_usa.csv'
file_path_17 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/tariffs_usa.csv'
file_path_18 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/trade_in_services_usa.csv'
file_path_19 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/data_world_bank/world_bank_data.csv'

# List containing all file path variables
all_files = [file_path_1, file_path_2, file_path_3, file_path_4, file_path_5, file_path_6, file_path_7, file_path_8, file_path_9, file_path_10, file_path_11, file_path_12, file_path_13, file_path_14, file_path_15, file_path_16, file_path_17, file_path_18, file_path_19]

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

df9 = pd.read_csv(file_path_9)
print(f'\nDataFrame 9 - First 5 Rows:')
print(df9.head())

df10 = pd.read_csv(file_path_10)
print(f'\nDataFrame 10 - First 5 Rows:')
print(df10.head())

df11 = pd.read_csv(file_path_11)
print(f'\nDataFrame 11 - First 5 Rows:')
print(df11.head())

df12 = pd.read_csv(file_path_12)
print(f'\nDataFrame 12 - First 5 Rows:')
print(df12.head())

df13 = pd.read_csv(file_path_13)
print(f'\nDataFrame 13 - First 5 Rows:')
print(df13.head())

df14 = pd.read_csv(file_path_14)
print(f'\nDataFrame 14 - First 5 Rows:')
print(df14.head())

df15 = pd.read_csv(file_path_15)
print(f'\nDataFrame 15 - First 5 Rows:')
print(df15.head())

df16 = pd.read_csv(file_path_16)
print(f'\nDataFrame 16 - First 5 Rows:')
print(df16.head())

df17 = pd.read_csv(file_path_17)
print(f'\nDataFrame 17 - First 5 Rows:')
print(df17.head())

df18 = pd.read_csv(file_path_18)
print(f'\nDataFrame 18 - First 5 Rows:')
print(df18.head())

df19 = pd.read_csv(file_path_19)
print(f'\nDataFrame 19 - First 5 Rows:')
print(df19.head())


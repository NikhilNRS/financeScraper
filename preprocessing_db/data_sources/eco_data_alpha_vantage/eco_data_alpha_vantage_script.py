import pandas as pd

# Generated Python script
file_path_1 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/durables_monthly_2024-02-26.csv'
file_path_2 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/unemployment_monthly_2024-02-26.csv'
file_path_3 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/real_gdp_quarterly_2024-02-26.csv'
file_path_4 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/cpi_monthly_2024-02-26.csv'
file_path_5 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/real_gdp_annual_2024-02-26.csv'
file_path_6 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/inflation_annual_2024-02-26.csv'
file_path_7 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/federal_funds_rate_weekly_2024-02-26.csv'
file_path_8 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/retail_sales_monthly_2024-02-26.csv'
file_path_9 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/treasury_yield_monthly_2024-02-26.csv'
file_path_10 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/federal_funds_rate_monthly_2024-02-26.csv'
file_path_11 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/treasury_yield_daily_2024-02-26.csv'
file_path_12 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/real_gdp_per_capita_quarterly_2024-02-26.csv'
file_path_13 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/cpi_semiannual_2024-02-26.csv'
file_path_14 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/treasury_yield_weekly_2024-02-26.csv'
file_path_15 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/federal_funds_rate_daily_2024-02-26.csv'
file_path_16 = '/Users/nikhilrazab-sekh/Desktop/data_extraction/raw_collected_data/eco_data_alpha_vantage/nonfarm_payroll_monthly_2024-02-26.csv'

# List containing all file path variables
all_files = [file_path_1, file_path_2, file_path_3, file_path_4, file_path_5, file_path_6, file_path_7, file_path_8, file_path_9, file_path_10, file_path_11, file_path_12, file_path_13, file_path_14, file_path_15, file_path_16]

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


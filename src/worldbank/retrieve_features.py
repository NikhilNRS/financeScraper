import wbdata
import pandas as pd
from datetime import datetime
import os

# Ensure the .data directory exists
data_directory = ".data"
os.makedirs(data_directory, exist_ok=True)

# Set the date range for the data collection
start_date = datetime(2015, 1, 1)
end_date = datetime(2023, 12, 31)

# Define the indicators to fetch from the World Bank database
indicators = {
    "NY.GDP.MKTP.KD.ZG": "GDP growth rate",
    "FP.CPI.TOTL.ZG": "Inflation rate",
    "SL.UEM.TOTL.ZS": "Unemployment rate",
    "NE.RSB.GNFS.CD": "Trade balance",
    # Add more indicators here as needed
    "BX.KLT.DINV.CD.WD": "Foreign direct investment",
    "IT.NET.USER.ZS": "Internet penetration"
    # Ensure to include monetary policies, financial market indicators, etc.
}

# Fetch the data without the convert_date argument
data = wbdata.get_dataframe(
    indicators=indicators,
    country=['US'],  # Example for fetching Netherlands data, adjust as needed
    date=(start_date, end_date)
)

# Reset index to make 'date' a column for easier CSV writing
data.reset_index(inplace=True)

# Save the data to a CSV file in the specified .data directory
csv_file_path = os.path.join(data_directory, "world_bank_economic_indicators_usa.csv")
data.to_csv(csv_file_path, index=False)

print(f"Data collected and saved to {csv_file_path}")

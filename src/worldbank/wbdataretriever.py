import wbdata
import datetime

# Set up the country and indicator you're interested in
countries = ["NL"]  # Netherlands
indicators = {"NY.GDP.MKTP.CD": "GDP (current US$)"}  # GDP in current US dollars

# Set up the date range
date_range = (datetime.datetime(2020, 1, 1), datetime.datetime(2020, 12, 31))

# Fetch the data from the World Bank API
data = wbdata.get_dataframe(
    indicators=indicators,
    country=countries,
    date=date_range,
    freq="Y",  # Yearly frequency
    parse_dates=True  # Convert date fields to datetime objects
)

# Reset the index to make "country" a column again, if necessary
data.reset_index(inplace=True)

# Save the data to a CSV file
csv_file_path = "world_bank_data.csv"
data.to_csv(csv_file_path, index=False)

print(f"Data successfully saved to {csv_file_path}")

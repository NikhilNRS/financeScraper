import wbdata
import pandas as pd

def fetch_and_save_indicators_to_csv(csv_file_path: str):
    # Fetch the list of all indicators from the World Bank API
    indicators = wbdata.get_indicators(source=2)  # Corrected to use get_indicators

    # Convert the list of indicators to a pandas DataFrame
    indicators_df = pd.DataFrame(indicators)

    # If you want to filter or select specific columns, you can do so here
    # For example, to keep only the 'id' and 'name' columns:
    indicators_df = indicators_df[['id', 'name']]

    # Save the DataFrame to a CSV file
    indicators_df.to_csv(csv_file_path, index=False)
    print(f"Indicators have been saved to {csv_file_path}")

# Specify the path to the CSV file where you want to save the indicators
csv_file_path = "world_bank_indicators.csv"

# Call the function with the specified CSV file path
fetch_and_save_indicators_to_csv(csv_file_path)

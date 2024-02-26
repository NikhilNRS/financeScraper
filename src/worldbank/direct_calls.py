import requests
import pandas as pd
import os

def fetch_world_bank_data(indicator, country='US', date_range='2015:2023'):
    base_url = "http://api.worldbank.org/v2/country"
    url = f"{base_url}/{country}/indicator/{indicator}?date={date_range}&format=json&per_page=500"
    response = requests.get(url)
    data = response.json()
    
    if len(data) > 1 and isinstance(data[1], list):
        df = pd.DataFrame(data[1])
        return df
    else:
        print(f"Error fetching data or no data returned for {indicator}")
        return pd.DataFrame()

def save_to_csv(df, filename, folder=".data"):
    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    
    # Save the DataFrame to a CSV file
    df.to_csv(filepath, index=False)
    print(f"Data successfully saved to {filepath}")

# Indicators of interest
# Extended Indicators of interest
indicators = {
    "NY.GDP.MKTP.KD.ZG": "gdp_growth_rates_usa.csv",
    "FP.CPI.TOTL.ZG": "inflation_rates_usa.csv",
    "SL.UEM.TOTL.ZS": "unemployment_rates_usa.csv",
    "FR.INR.RINR": "central_bank_policy_rates_usa.csv",
    "NE.RSB.GNFS.CD": "trade_balance_usa.csv",
    "TM.TAX.MRCH.SM.AR.ZS": "tariffs_usa.csv",
    "BG.GSR.NFSV.GD.ZS": "trade_in_services_usa.csv",
    "CM.MKT.INDX.ZG": "stock_market_indices_usa.csv",
    # Note: Gold prices and other commodity prices might not be available directly from World Bank data
    "BX.KLT.DINV.CD.WD": "foreign_direct_investment_usa.csv",
    "BM.KLT.DINV.GD.ZS": "portfolio_investment_usa.csv",
    "BX.TRF.PWKR.DT.GD.ZS": "remittances_usa.csv",
    "IT.NET.USER.ZS": "internet_penetration_usa.csv",
    # Added indicators
    "GC.DOD.TOTL.GD.ZS": "total_public_debt_gdp_usa.csv",
    "FS.AST.PRVT.GD.ZS": "domestic_credit_private_sector_usa.csv",
    # For technology adoption and digital economy - surrogate indicators
    "IT.CEL.SETS.P2": "mobile_cellular_subscriptions_usa.csv",
    # Note: Specific measures for energy prices, regulatory environment, and economic sentiment may need to be sourced elsewhere
}

# Fetch and save data for each indicator
for indicator, filename in indicators.items():
    df = fetch_world_bank_data(indicator)
    if not df.empty:
        save_to_csv(df, filename)
    else:
        print(f"No data available for {indicator}")

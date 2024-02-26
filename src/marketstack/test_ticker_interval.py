import requests

def test_ticker_interval(api_key, ticker, interval):
    base_url = "http://api.marketstack.com/v1/eod" if interval == "daily" else "http://api.marketstack.com/v1/intraday"
    params = {
        'access_key': api_key,
        'symbols': ticker,
        'limit': 1
    }
    if interval != "daily":
        params['interval'] = interval
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        print(f"Success: Data available for {ticker} at {interval} interval.")
    else:
        print(f"Error: Data not available for {ticker} at {interval} interval. Response code: {response.status_code}")

# Example usage
api_key = 'your-api-key'
tickers = ['PHAU.XLON', 'GSPC.INDX', 'DJI.INDX']
intervals = ['1hour', '6hour', 'daily']

for ticker in tickers:
    for interval in intervals:
        test_ticker_interval(api_key, ticker, interval)

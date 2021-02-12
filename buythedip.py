import requests 
import json
import pandas as pd 

if __name__ == '__main__':
    API_KEY = 'NS51XYA5B1AT6BNJ'

def daily_ticker_data(ticker):
	r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}')
	data = json.loads(r.content.decode('utf-8'))
	df = pd.DataFrame.from_dict(data['Time Series (Daily)'])
	df = df.rename({'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
	return df

def intra_daily_ticker_data(ticker):
	r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={API_KEY}&outputsize=full')
	data = json.loads(r.content.decode('utf-8'))
	df = pd.DataFrame.from_dict(data['Time Series (5min)'])
	df = df.rename({'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
	return df

ticker = daily_ticker_data('KMI')
print(ticker)

ticker.to_pickle("./KMI_daily.pkl")

intra_ticker = intra_daily_ticker_data('KMI')
print(list(intra_ticker))

intra_ticker.to_pickle("./KMI_intra.pkl")

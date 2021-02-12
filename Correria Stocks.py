import bs4 as bs
import pandas as pd
import numpy as np 
import locale
import yfinance as yf 
import seaborn as sns 
import matplotlib.pyplot as plt 
import os 

pd.set_option('display.max_columns', 500)
# PEG_tables = pd.DataFrame()
# for x in range(2, 100, 2):
# 	# do the thing from the other stock program, up to 500
# 	temp = pd.read_html(f'https://finviz.com/screener.ashx?v=1&o=peg&r={x}1')[-2]
# 	PEG_tables = pd.concat([PEG_tables, temp])
# PEG_tables.reset_index(drop=True)
# PEG_tables.to_csv('PEG_tables.csv')

PEG_tables = pd.read_csv('PEG_tables.csv')

new_columns = PEG_tables.iloc[0]
# remove first row of PEG_tables
PEG_tables.columns = new_columns
PEG_tables = PEG_tables.iloc[1:]
PEG_tables.drop('No.', axis=1, inplace=True)

# then do the other ones from the notes 

sharpe = pd.read_csv('Sharpe Ratio Stocks Landing Page.csv')
sharpe = sharpe.sort_values(by=['Sharpe Ratio'])[['Ticker', 'Sharpe Ratio']]

sharpe = sharpe[sharpe['Sharpe Ratio'] >= 1.00]

# can i use .loc[] to for all sharpe['Ticker']
# print(PEG_tables.loc[(PEG_tables['Ticker'].isin(sharpe['Ticker']))]['Ticker'])
# print(PEG_tables['Ticker'].isin(sharpe['Ticker'].values))

# now calculate sharpe ratio for all 5000, can do that through a calculation, how many years sharpe ratio

# print(pd.read_html('https://lol.gamepedia.com/LCK/2019_Season/Regional_Finals/Picks_and_Bans'))

with open('tickers.txt', 'r') as file:
	tickers = file.read().split(' ')
# for ticker in tickers[2475:2500]:
# 	print(ticker)
# 	df = yf.download(ticker,'2015-09-01','2019-09-21')
# 	df.to_csv(f'All_Stocks/{ticker}.csv')
directory = os.fsencode('All_Stocks')
directory = os.listdir(directory)

stocks = []
for ticker in directory:
	ticker = ticker.decode('ascii')
	stocks.append([ticker, pd.read_csv('All_Stocks/'+ticker)])
	# if df['Volume'].mean() < 50_000:
	# 	os.remove(ticker)

# nok = directory.index(b'NOK.csv')
# nok = stocks[nok]
# first_date = nok.index[nok['Date'] == '2015-09-21'].tolist()[0]
# last_date = nok.index[nok['Date'] == '2019-09-20'].tolist()[0]
# nok = nok.iloc[first_date:last_date]
# print(sorted(((nok['High'] - nok['Low']) / nok['Low'])))

# do a sorted by percent change, have list [ticker, pct change]
for stock in stocks:
	ticker, df = stock
	first_date = df.index[df['Date'] == '2015-09-21'].tolist()[0]
	last_date = df.index[df['Date'] == '2019-09-10'].tolist()[0]
	df = df.iloc[first_date:last_date]
	df = df.reset_index()['Adj Close']
	investment_return = df.tail(1) - df.head(1)
	l = []
	for x in range(len(df)-1):
		l.append((df.iloc[x+1] - df.iloc[x]) / df.loc[x])
	ann_std = np.std(l) * (0.5 ** 252)
	print(ticker, investment_return / ann_std)

def recursive(x):
	x += 1
	if x == 10:
		return x 
	else:
		return recursive(x) ** 2
# print(recursive(1))






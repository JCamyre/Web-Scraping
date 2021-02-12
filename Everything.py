from requests import get
import bs4 as bs
import pandas as pd
import numpy as np 
import locale 

pd.set_option('display.max_columns', 500)

# price2earnings = get('https://finviz.com/screener.ashx?v=152&o=-pe&r=1')
# soup1 = bs.BeautifulSoup(price2earnings.text, 'lxml')

# price2sales = get('https://finviz.com/screener.ashx?v=152&o=-ps&r=1')
# soup2 = bs.BeautifulSoup(price2sales.text, 'lxml')

def get_dict(soup):
	wack1 = []
	wack2 = []
	for x in range(0, 2, 2):
		table = soup.find('table', {'bgcolor': '#d3d3d3'})
		rows = table.find_all('td')
		wack1 = [x.get_text() for x in rows[:11:]]
		for x in range(len(rows))[11::11]:
			# Append the market cap of all to one thing, then we can use wack1 to get the {'Market Cap': '['320M', '400B']'} 
			wack2 += [y.get_text() for y in rows[x:x+11:]]
			
	# ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']		
	
	dic = {}
	# len(dic.items()) == 11
	for x in range(len(wack1)):
		key = wack1[x]
		dic[key] = [x for x in wack2[x::11]]
		# print([x for x in wack2[x::11]])

	final_dic = []
	for index in range(20):
		temp = {}
		for key, vals in dic.items():
			temp[key] = vals[index]
		final_dic.append(temp)
	return final_dic

def make_df(name, signal, num):
	list1 = []
	for num in range(0, num//11 + 1, 2):
		request = get(f'https://finviz.com/screener.ashx?v=152&o=-{signal}&r={num}1')
		soup1 = bs.BeautifulSoup(request.text, 'lxml')
		s1 = get_dict(soup1)
		for y in [x for x in s1]:
			list1.append([y[z] for z in y])
	df1 = pd.DataFrame(list1,
		columns=['No.', 'Ticker', 'Company', 'Sector', 'Industry', 'Country', 'Market Cap', 'P/E', 'Price', 'Change', 'Volume'])
	df1.to_csv(f'Stats/{name}')

# for signal in ['pe', 'ps', 'perfytd', 'eps', 'epsyoy']:
# 	make_df(signal, signal, 400)

folder = 'Stats/'
eps = pd.read_csv(folder + 'eps')
# epsyoy = pd.read_csv(folder + 'epsyoy')
# epsyoy = [ticker for ticker in epsyoy['Ticker'].values]

# low p/e means good value for their earnings, however might mean low confidence in company
# pe = pd.read_csv(folder + 'pe')
# pe = [ticker for ticker in pe['Ticker'].values]
# perfytd = pd.read_csv(folder + 'perfytd')
# perfytd = [ticker for ticker in perfytd['Ticker'].values]
# ps = pd.read_csv(folder + 'ps')
# ps = [ticker for ticker in ps['Ticker'].values]

# stocks = []
# for ticker in eps['Ticker'].values:
# 	if ticker in epsyoy and pe and perfytd and ps:
# 		stocks.append(ticker)

# with open('Stats/stocks', 'w') as file:
# 	for stock in stocks:
# 		file.write(stock + ', ')
s = []
# needed to convert string with comma to int
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

with open('Stats/stocks', 'r') as file:
	stocks = file.read().split()
	for stock in stocks:
		stock = stock[:-1]
		if locale.atoi(eps[eps['Ticker'] == stock].values[0][-1]) > 50000:
			s.append(stock)

		# if (eps['Ticker'] == stock).any():
		# 	print((eps.stock))
		# if stock's avg volume over 50000, add to s
		# if eps['Ticker'] == stock 
		# 	s.append(stock)

with open('Stats/stocks', 'w') as file:
	for x in s:
		file.write(x + ', ')	

# for stock in stocks:
# 	print(eps[eps['Ticker'] == stock].values[0][3])
	# print(eps[eps['Ticker'] == stock].values)
	# print(list(eps[eps['Ticker'] == stock].values[0])[2:])


# merge1 = pd.merge(eps, pe, on=['Ticker'], how='inner')
# for x in range(len(merge1)):
# 	print(f"{merge1['Ticker'][x]}: ${merge1['Price_x'][x]}, {merge1['Market Cap_x'][x]}")
# print('*' * 40)
# merge2 = pd.merge(perfytd, epsyoy, on=['Ticker'], how='inner')
# for x in range(len(merge2)):
# 	print(f"{merge2['Ticker'][x]}: ${merge2['Price_x'][x]}, {merge2['Market Cap_x'][x]}")
# print('*' * 40)
# merged = pd.merge(merge1, merge2, on=['Ticker'], how='inner')
# for x in range(len(merged)):
# 	print(f"{merged['Ticker'][x]}: ${merged['Price_x_x'][x]}, {merged['Market Cap_x_x'][x]}")


# for x in [folder + x for x in ['epsyoy', 'pe', 'perfytd', 'ps']]:
# 	print(pd.read_csv(x)['Ticker'])


# write the dictionaries and add a space
# list1 = []
# for num in range(0, 11, 2):
# 	price2earnings = get(f'https://finviz.com/screener.ashx?v=152&o=-pe&r={num}1')
# 	soup1 = bs.BeautifulSoup(price2earnings.text, 'lxml')
# 	s1 = get_dict(soup1)

# 	# maybe i can do to_csv in here, or mass combine at end? 

# 	for y in [x for x in s1]:
# 		list1.append([y[z] for z in y])
# 	df1 = pd.DataFrame(list1,
# 		columns=['No.', 'Ticker', 'Company', 'Sector', 'Industry', 'Country', 'Market Cap', 'P/E', 'Price', 'Change', 'Volume'])
# 	df1.to_csv('p2e')



# 	# df1.append(df_temp)

# 	# for x in [key for key in s1[0]]:
# 	# 	print([key[x] for key in s1])
# 	# 	list1.append([key[x] for key in s1])
# 	# print(len(np.array(list1)))
# 	# print(len([key for key in s1[0]]))
# 	# ok so 11 keys, but 20 vals each, is it confused?
# 	# temp_df = pd.DataFrame(list1, columns=[key for key in s1[0]])

# 	# print([np.array(arr) for arr in list1])
# 	# for x in [arr for arr in list1]:
# 	# 	print(np.array(x))


# 	# dic for dic in s1 for key in dic
# 	# print([key['Ticker'] for key in s1])
# 	for x in s1:
# 		for y in x:
# 			pass
# 			# print(y, x[y])
# 	# with open('Stats/pe.txt', 'w') as f:
# 	# 	for x in s1:
# 	# 		f.write(str(x) + '\n')
# 	# df_temp = pd.DataFrame(columns=[[key for key in s1[0]]])

# # maybe make this a function, and have parameters for a name for the file and idk whatelse
# df1 = pd.DataFrame(list1,
# 	columns=['No.', 'Ticker', 'Company', 'Sector', 'Industry', 'Country', 'Market Cap', 'P/E', 'Price', 'Change', 'Volume'])
# df1.to_csv('p2e')

# for num in range(0, 11, 2):
# 	price2sales = get(f'https://finviz.com/screener.ashx?v=152&o=-ps&r={num}1')
# 	soup2 = bs.BeautifulSoup(price2sales.text, 'lxml')
# 	s2 = get_dict(soup2)


# for num in range(0, 11, 2):
# 	highytd = get(f'https://finviz.com/screener.ashx?v=152&o=-perfytd&r={num}1')
# 	soup3 = bs.BeautifulSoup(highytd.text, 'lxml')
# 	s3 = get_dict(soup3)


# for num in range(0, 11, 2):
# 	earningspershare = get('https://finviz.com/screener.ashx?v=152&o=-eps&r=1')
# 	soup4 = bs.BeautifulSoup(earningspershare.text, 'lxml')
# 	s4 = get_dict(soup4)


# for num in range(0, 11, 2):
# 	earningspersharethisyear = get('https://finviz.com/screener.ashx?v=152&o=-epsyoy&r=1')
# 	soup5 = bs.BeautifulSoup(earningspersharethisyear.text, 'lxml')
# 	s5 = get_dict(soup5)


# s1, s2, s3, s4, s5 = [], [], [], [], []
# with open('Stats/eps.txt', 'r') as f:
# 	for x in f.readlines():
# 		s1.append(x[:-1])

# with open('Stats/epsty.txt', 'r') as f:
# 	for x in f.readlines():
# 		s2.append(x[:-1])


# with open('Stats/pe.txt', 'r') as f:
# 	for x in f.readlines():
# 		s3.append(x[:-1])


# with open('Stats/ps.txt', 'r') as f:
# 	for x in f.readlines():
# 		s4.append(x[:-1])


# with open('Stats/ytd.txt', 'r') as f:
# 	for x in f.readlines():
# 		s5.append(x[:-1])


# now just compare all dicts, and if a ticker is in all five, add it to a new list of dictionaries

# earningspershare = get('https://finviz.com/screener.ashx?v=152&o=-eps&r=1')
# soup4 = bs.BeautifulSoup(earningspershare.text, 'lxml')

# earningspersharethisyear = get('https://finviz.com/screener.ashx?v=152&o=-epsyoy&r=1')
# soup5 = bs.BeautifulSoup(earningspersharethisyear.text, 'lxml')
	
# def recur(n):
# 	if n == 1:
# 		return n
# 	else:
# 		return recur(n-1) * n

# print(recur(6))


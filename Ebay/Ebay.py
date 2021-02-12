from requests import get 
from bs4 import BeautifulSoup
import re
import statistics
import pickle

base_url = 'https://www.ebay.com/sch/i.html?_from=R40'
# &LH_All=1&LH_Sold=1&rt=nc
url = f'{base_url}&_nkw=c920'

def find_prices(item_name, auction_only=False) -> list:
	auction = '0' if auction_only else '1'
	all_items = []
	for i in range(1, 30):
		url = f'{base_url}&_nkw={item_name}&LH_Sold=1&LH_ALL={auction}&_ipg=50&rt=nc&Model=Logitech%2520C920&_oaa=1&_dcat=4616&_pgn={i}'
		page = get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		items = soup.find_all('div', {'class': 's-item__details clearfix'})
		pattern = re.compile(r'\d*\.\d*')
		item_prices = [float(pattern.search(item.get_text()).group(0)) for item in items]
		all_items.append(item_prices)
		# adj_item_prices = sorted(item_prices)[10:-2]
		# print(sum(adj_item_prices) // len(adj_item_prices))
		# print(statistics.median(adj_item_prices), statistics.mode(adj_item_prices), statistics.mode(adj_item_prices), statistics.median_grouped(adj_item_prices))
		# print(len(adj_item_prices))
		# print(url)
	return all_items

def save_prices():
	item_prices = find_prices('C920')
	filename = 'C920'

	with open(filename, 'wb') as file:
		pickle.dump(item_prices, file)

def read_prices():
	filename = 'C920'

	with open(filename, 'rb') as file:
		item_prices = pickle.load(file)

	for i, items in enumerate(item_prices):
		print(i, sum(items)/50)

	item_prices = [item for items in item_prices[:8]
						for item in items]
	item_prices = sorted(item_prices)[40:-10]
	print(statistics.mean(item_prices), statistics.median(item_prices), statistics.median_grouped(item_prices), statistics.mode(item_prices))

read_prices()


import pandas as pd 
from requests import get 
import bs4 as bs

pd.set_option('display.max_columns', 500)


request = get('https://stardewvalleywiki.com/Crops')
soup = bs.BeautifulSoup(request.text, 'lxml')
tables = soup.find_all('table', {'class': 'wikitable'})
for table in tables[2:-1]:
	table = pd.read_html(str(table))[0]
	print(table)
	print('*' * 80)


from requests import get
import bs4 as bs 
import pandas as pd

pd.set_option('display.max_columns', 25)
# pd.set_option('display.width', 1000)

request = get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population_density')
soup = bs.BeautifulSoup(request.text, 'lxml')
tables = soup.find_all('table')
for table in tables:
	# Populationdensity(people per mi2), Cities
	df = pd.read_html(str(table))[0]
	print(df.columns.values)
	print('*')
	# df = df[['Populationdensity(people per mi2)', 'Cities']]


# request = get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate')
# soup = bs.BeautifulSoup(request.text, 'lxml')
# table = soup.find('table')
# df = pd.read_html(str(table))[0]
# print(df)


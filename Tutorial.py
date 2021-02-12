import bs4 as bs 
import urllib.request
import pandas as pd

source = urllib.request.urlopen('https://play.typeracer.com')
soup = bs.BeautifulSoup(source,'lxml')

tables = soup.find_all('table')

for table in tables:
	print([x.get('href') for x in table.find_all('a')])

dfs = pd.read_html('https://play.typeracer.com', header=0)
for df in dfs:
	print(df)


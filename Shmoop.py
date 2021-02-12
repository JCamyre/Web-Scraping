from requests import get 
import bs4 as bs
import pandas as pd 

request = get('https://www.shmoop.com/catcher-in-the-rye/characters.html')
soup = bs.BeautifulSoup(request.text, 'lxml')
divs = soup.find_all('div', {'class': 'panel-heading'})

for i, name in enumerate(divs):
	print(i, ': ' + name.get_text())


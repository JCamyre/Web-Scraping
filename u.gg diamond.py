import bs4 as bs 
from requests import get 

request = get('https://u.gg/lol/tier-list/?role=jungle&rank=diamond')
soup = bs.BeautifulSoup(request.text, 'lxml')
# div = soup.find('div', {'style': 'display: flex'})
print(soup.get_text())



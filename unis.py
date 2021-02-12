from requests import get
import bs4 as bs 

request = get('https://blog.prepscholar.com/schools-that-require-the-sat-essay')
soup = bs.BeautifulSoup(request.text, 'lxml')

table = soup.find('table')
td = table.find_all('td')
with open('unis.txt', 'w') as file:
	for x in range(len(td))[::3]:
		file.write(f'{td[x].text}, {td[x+1].text}: {td[x+2].text}' + '\n' * 2)



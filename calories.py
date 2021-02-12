from requests import get
import bs4 as bs

request = get('https://www.nutrition-charts.com/mcdonalds-nutrition-facts-calorie-information/')
soup = bs.BeautifulSoup(request.text, 'lxml')
table = soup.table
body = table.find('tbody')
rows = body.find_all('td')
rows = [x.get_text() for x in rows if 'back to top' not in x and x != '']
dict = {}
for x in rows:
	print(x)
	print(type(x))

# for x in range(len(rows)):
# 	print(x, rows[x].get_text())

from requests import get
import bs4 as bs
import urllib.request

def get_data():
    resp = get('https://stardewvalleywiki.com/Bundles')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    return soup

soup = get_data()

# print([x.text for x in soup.find_all('table')])

# for x in soup.find_all('table'):
# 	print(x.text)

# print([x.get('href') for x in soup.find_all('a')])

table = soup.find_all('table', {'class': 'wikitable'})


	# print(row.find_all('span', {'id': 'nametemplate'}))	

# tbl = soup.find('table')
# table_rows = tbl.find_all('tr')

# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

# for url in soup.div.find_all('a'):
# 	print(url.get('href'))

# print(soup.find_all('p'))
# return table 

# def lisp(text):
# 	for word in text:
# 		if word[:-2]:
# 			word = word[]





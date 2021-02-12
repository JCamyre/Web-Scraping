from requests import get
import bs4 as bs
import os

directory_in_str = 'Stocks'

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith('.txt'):
     	with open(f'Stocks/{filename}', 'r') as file:
     		print(filename[:-4])
     		a = file.read().split()
     		dict = {}
     		for x in range(len(a)-1)[::2]:
     			print(a[x][:-1])
     			dict[a[x][:-1]] = a[x+1]
     		print(dict)


# ticker = 'NEPT'
# request = get(f'https://finviz.com/quote.ashx?t={ticker}&ty=c&ta=1&p=d')
# soup = bs.BeautifulSoup(request.text, 'lxml')

# title_table = soup.find('table', {'class': 'fullview-title'})
# title_table = title_table.find('a').get_text()

# data_table = soup.find('table', {'class': 'snapshot-table2'})
# td = data_table.find_all('td')
# with open(f'Stocks/{title_table}.txt', 'w') as file:
# 	for index in range(len(td))[::2]:
# 		file.write(str(td[index].text) + ': ' + str(td[index+1].text) +'\n')
# run a loop 

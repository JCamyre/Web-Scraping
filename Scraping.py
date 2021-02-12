# from requests.exceptions import RequestException
# from contextlib import closing
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
#ijjj
#
# def simple_get(url):
#     """
#     Attempts to get the content at `url` by making an HTTP GET request.
#     If the content-type of response is some kind of HTML/XML, return the
#     text content, otherwise return None.
#     """
#     try:
#         with closing(get(url, stream=True)) as resp:
#             if is_good_response(resp):
#                 return resp.content
#             else:
#                 return None
#
#     except RequestException as e:
#         log_error('Error during requests to {0} : {1}'.format(url, str(e)))
#         return None
#
#
# def is_good_response(resp):
#     """
#     Returns True if the response seems to be HTML, False otherwise.
#     """
#     content_type = resp.headers['Content-Type'].lower()
#     return (resp.status_code == 200
#             and content_type is not None
#             and content_type.find('html') > -1)
#
#
# def log_error(e):
#     """
#     It is always a good idea to log errors.
#     This function just prints them, but you can
#     make it do anything.
#     """
#     print(e)
#
#
# raw_html = simple_get('https://realpython.com/blog/')
#
#
# html = BeautifulSoup(raw_html, 'html.parser')
# for div in html.select('div'):
#     if div['id'] == 'main':
#         print(div.text)
#     print(div)



# page = get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
#
# soup = BeautifulSoup(page.text, 'html.parser')
#
# last_links = soup.find(class_='AlphaNav')
# last_links.decompose()
#
# artist_name_list = soup.find(class_='BodyText')
# artist_name_list_items = artist_name_list.find_all('a')
#
# # Use .contents to pull out the <a> tag’s children
# for artist_name in artist_name_list_items:
#     names = artist_name.contents
#     print(names)
# # My site
# my_site = get('https://howtobecomeaprogrammer.neocities.org')
#
# s = BeautifulSoup(my_site.text, 'html.parser')
# center = s.find(class_='container')
# center_p = center.find_all('p')
#
# for x in center_p:
#     print(x)
# Type_racer
type_racer = get('https://data.typeracer.com/pit/race_history?user=itypesomewhatalot&n=100&startDate=')

with open('typeracer.txt', '+w') as line:
    line.write(type_racer.text)

c = 0
with open('typeracer.txt', 'r') as raw_html:
    html = BeautifulSoup(raw_html, 'html.parser')
    f = html.find_all('td')
list1 = []
list2 = []
for x in range(len(f)):
    if 'WPM' in str(f[x]):
        print(len(str(f[x])))
        x = int(str(f[x])[4:len(str(f[x]))-9])
        list1.append(x)
print(sum(list1)/len(list1))
# for x in list1:
#     list2.append(int(x[:3]))
# print(sum(list2)/len(list2))
for table in html.select('table'):
    print()

type_racer_soup = BeautifulSoup(type_racer.text, 'html.parser')
typing = type_racer_soup.find(class_='scoresTable')
typing_f = typing.find_all('td')



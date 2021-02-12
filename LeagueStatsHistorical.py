import time

from selenium import webdriver
from selenium.webdriver.chrome import service


webdriver_service = service.Service('C:/Users/JWcam/Downloads/operadriver_win64/operadriver_win64/operadriver.exe')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
driver.maximize_window()
driver.get('https://u.gg/lol/tier-list')
assert 'u.gg' in driver.title
time.sleep(4)
cookie_accept = driver.find_element_by_class_name('qc-cmp-button').click()
time.sleep(1.5)

ranks = driver.find_elements_by_class_name('rank-option')[1]
print(ranks)
ranks.click()
time.sleep(0.5)
rank = driver.find_elements_by_css_selector('.default-select__control.css-fdnumy')
print([division.text for division in rank])
# sidebar = driver.find_elements_by_class_name('site-navigator')
# print([div.find_elements_by_class_name for div in sidebar])
# tierlist = driver.find_elements_by_tag_name('a')
# print([element.text for elements in tierlist for element in elements])
# input_txt.send_keys('www.youtube.com')
# input_txt.send_keys('\n')

time.sleep(100) #see the result
driver.quit()

divisions = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Challenger', 'Platinum_plus', 'Diamond_plus']
for division in divisions:
	pass

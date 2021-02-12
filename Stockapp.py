import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from requests import get
import bs4 as bs
import os

# Maybe add create a stock folder

class Page(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1

		self.input = TextInput()
		self.add_widget(self.input)

		self.btn = Button(text='Enter a stock')
		self.btn.bind(on_press=self.get_stock)
		self.add_widget(self.btn)

	def get_stock(self, _):
		# newpath = r'C:\Program Files\arbitrary' 
		# 	if not os.path.exists(newpath):
		# 	    os.makedirs(newpath)
		if self.input.text:
			ticker = self.input.text
			request = get(f'https://finviz.com/quote.ashx?t={ticker}')
			soup = bs.BeautifulSoup(request.text, 'lxml')

			title_table = soup.find('table', {'class': 'fullview-title'})
			title_table = title_table.find('a').get_text()

			data_table = soup.find('table', {'class': 'snapshot-table2'})
			td = data_table.find_all('td')
			with open(f'Stocks/{title_table}.txt', 'w') as file:
				for index in range(len(td))[::2]:
					file.write(str(td[index].text) + ': ' + str(td[index+1].text) +'\n')

class EpicApp(App):
	def build(self):
		self.screen_manager =ScreenManager()
		self.page = Page()
		screen = Screen(name='Page')
		screen.add_widget(self.page)
		self.screen_manager.add_widget(screen)

		return self.screen_manager

if __name__ == '__main__':
	app = EpicApp()
	app.run()


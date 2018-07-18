#https://www.marketwatch.com/tools/stockresearch/updown



import re

import requests
from bs4 import BeautifulSoup

def stocks_analyst_action():

	dataurl = "https://www.marketwatch.com/tools/stockresearch/updown"

	results = set()

	page = requests.get(dataurl)
	soup = BeautifulSoup(page.text, 'html.parser')
	table = soup.find("table",{"class":"tablesorter"})

	for row in table.find_all('tr'):
		cells = row.find_all('td')
		if len(cells) >1 :
			ticker = (cells[1].text)
			results.add(ticker.strip('\n').strip())

	return list(results)




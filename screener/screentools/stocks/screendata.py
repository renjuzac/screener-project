from screentools.stocks import  scan
from screentools.stocks import  scraper

def stocks_52wk_high():
	stocks = scraper.stocks_52wk_highlow()
	return stocks['high']

def stocks_52wk_low():
	stocks = scraper.stocks_52wk_highlow()
	return stocks['low']

def scan_on_growth():
	return scan.scan_on_growth()
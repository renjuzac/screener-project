from screentools.stocks import  scan
from screentools.stocks import  scraper
from screentools.stocks import fetch
from screentools.stocks import analyst_scraper

def stocks_52wk_high():
	stocks = scraper.stocks_52wk_highlow()
	return stocks['high']

def stocks_52wk_low():
	stocks = scraper.stocks_52wk_highlow()
	return stocks['low']

def scan_on_growth():
	return scan.scan_on_growth()

def scan_on_declining_growth():
	stocks = fetch.get_stocks_with_declining_revenue()
	return list(stocks.keys())

def scan_for_momentum():
	stocks = fetch.get_stocks_passing_minimum_criteria()
	one_yr_returns = fetch.get_one_yr_change_stocks(stocks)
	return sorted(one_yr_returns, key=one_yr_returns.get, reverse=True)[:50]

def analyst_rating_updown():
	return analyst_scraper.stocks_analyst_action()






# https://stackoverflow.com/questions/7197315/5-maximum-values-in-a-python-dictionary
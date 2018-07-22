from screentools.stocks import fetch_intrinio
from screentools.stocks import scan
from screentools.stocks import fetch_barchart
from screentools.stocks import fetch_quandl
from screentools.stocks import fetch_iex


# https://api.intrinio.com/financials/standardized?identifier=AAPL&statement=income_statement&type=FY&date=2018-01-01
# TODO Check option for only close data from Barchart

symbols = ['AAPL', 'GOOGL']
fields = ["fiftyTwoWkHigh", "fiftyTwoWkLow", "avgVolume", "twentyDayAvgVol"]


def getquote(symbols=symbols, fields=fields):
    return fetch_barchart.getquote(symbols=symbols, fields=fields)


def get_stocks_with_revenue_growth_over(percent):
    return fetch_intrinio.get_stocks_with_revenue_growth_over(percent)

def get_stocks_with_declining_revenue(percent=0):
	return fetch_intrinio.get_stocks_with_declining_revenue(percent)

def get_stocks_passing_minimum_criteria(percent = 0):
	return fetch_intrinio.get_stocks_passing_minimum_criteria(percent = 0)

#def get_revenue_growth(stock_list):
#	return fetch_intrinio.get_revenue_growth(stock_list)

def	get_revenue_growth(stocklist):
	return fetch_quandl.get_revenue_growth(stocklist)


def get_stock_price_and_vol(stock_list):
    return fetch_intrinio.get_stock_price_and_vol(stock_list)


def get_aq_multiple_stock(stock):
	return fetch_quandl.get_aq_multiple_stock(stock)

def	get_aq_multiple_stock_list(stocklist):
	return fetch_quandl.get_aq_multiple_stock_list(stocklist)

def get_enterprise_multiple(stocklist):
	return fetch_quandl.get_enterprise_multiple(stocklist)

def get_metadata(stock):
	return fetch_quandl.get_metadata(stock)


def get_one_yr_change(ticker):
	return fetch_iex.get_one_yr_change(ticker)

def get_one_yr_change_stocks(tickers_list):
	return fetch_iex.get_one_yr_change_stocks(tickers_list)
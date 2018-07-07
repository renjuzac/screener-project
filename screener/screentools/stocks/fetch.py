from screentools.stocks import fetch_intrinio
from screentools.stocks import scan
from screentools.stocks import fetch_barchart
from screentools.stocks import fetch_quandl


# https://api.intrinio.com/financials/standardized?identifier=AAPL&statement=income_statement&type=FY&date=2018-01-01
# TODO Check option for only close data from Barchart

symbols = ['AAPL', 'GOOGL']
fields = ["fiftyTwoWkHigh", "fiftyTwoWkLow", "avgVolume", "twentyDayAvgVol"]


def getquote(symbols=symbols, fields=fields):
    return fetch_barchart.getquote(symbols=symbols, fields=fields)


def get_stocks_with_revenue_growth_over(percent):
    return fetch_intrinio.get_stocks_with_revenue_growth_over(percent)


def get_stock_price_and_vol(stock_list):
    return fetch_intrinio.get_stock_price_and_vol(stock_list)



def get_aq_multiple_stock(stock):
	return fetch_quandl.get_aq_multiple_stock(stock)

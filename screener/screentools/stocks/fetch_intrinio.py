from datetime import timedelta

#import requests
import json

from . import caching
from ..config import username,password

ticker = "NTNX"


def get_url(url):
    try:
#        response = requests.get(url, auth=(username, password))
        response = caching.session.get(url, auth=(username, password))
        results = json.loads(response.text)
        return results

    except Exception as e:
        print("Error fetching data from server :- {}".format( url))
#        print ("Response string:{}".format(response.text))
        return {}





def get_stocks_with_revenue_growth_over(percent ):
    ''' e.g.  percent="0.3"  (is 30% )
    API returns first 150 by default
    API e.g.  'result_count': 714, 'page_size': 100, 'current_page': 1, 'total_pages': 8,'''
    page_number = 1
    total_pages = 1
    base_url = "https://api.intrinio.com/securities/search?conditions=revenuegrowth~gt~{}&page_number={}"
    try:
        stocks = {}
        while page_number <= total_pages:
            search_url = base_url.format(percent, page_number)
            results = get_url(search_url)
            total_pages = results["total_pages"]
            for item in results["data"]:
                stocks.update({item['ticker'] :item['revenuegrowth']})
            page_number += 1

        return stocks

    except Exception as e:
        print ("{}Error fetching data from server {}".format(e,base_url))
        return {}

def get_stock_price_and_vol(stock_list):
    base_url = "https://api.intrinio.com/securities/search?conditions=close_price~gt~15,average_daily_volume~gt~1000000&page_number={}"

    page_number = 1
    total_pages = 1
    stocks = {}
    while page_number <= total_pages:
        search_url = base_url.format(page_number)
        results = get_url(search_url)
        total_pages = results["total_pages"]
        for item in results["data"]:
            stocks.update({item['ticker']: item['close_price']})
        page_number += 1

    return stocks




def get_aq_multiple_stock(stock):

    op_income_url = "https://api.intrinio.com/data_point?identifier={}&item=totaloperatingincome"
    ev_url = "https://api.intrinio.com/data_point?identifier={}&item=enterprisevalue"

    op_income_url = op_income_url.format(stock)
    ev_url = ev_url.format(stock)

    op_income_results = get_url(op_income_url)
    ev_results = get_url(ev_url)
    try:
        result = round(ev_results["value"] /op_income_results["value"],2)
    except TypeError:
        print("ev",ev_results["value"],"oe:",op_income_results["value"],op_income_results["identifier"])
        result = 0

    return result 


def get_aq_multiple(stock_list):

    op_income_url = "https://api.intrinio.com/data_point?identifier={}&item=totaloperatingincome"
    ev_url = "https://api.intrinio.com/data_point?identifier={}&item=enterprisevalue"

    stocks = ",".join(stock_list)
    op_income_url = op_income_url.format(stocks)
    ev_url = ev_url.format(stocks)

    op_income_results = get_url(op_income_url)
    ev_results = get_url(ev_url)

    results = {}

    for op_income,ev in zip(op_income_results['data'],ev_results['data']):
        assert (op_income["identifier"] == ev["identifier"])
        ticker = op_income["identifier"]
        results[ticker] = round(ev["value"] /op_income["value"],2)

    return results 


# {
#   "data": [
#     {
#       "identifier": "TNTR",
#       "item": "totaloperatingincome",
#       "value": -149466000
#     },
#     {
#       "identifier": "AAPL",
#       "item": "totaloperatingincome",
#       "value": 66056000000
#     }
#   ],
#   "result_count": 2,
#   "api_call_credits": 2
# }
# https://www.nasdaq.com/symbol/pstg/financials?query=income-statement Jan 2018 
# https://api.intrinio.com/data_point?identifier=NTNX&item=enterprisevalue




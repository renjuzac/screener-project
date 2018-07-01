from datetime import timedelta

#import requests
import json

from .caching import session
from config import username,password

ticker = "NTNX"


def get_url(url):
    try:
#        response = requests.get(url, auth=(username, password))
        response = session.get(url, auth=(username, password))
        results = json.loads(response.text)
        return results

    except Exception as e:
        print("Error fetching data from server :- {}".format( base_url))
        print ("Response string:{}".format(response.text))
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





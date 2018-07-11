
# https://iextrading.com/developer/docs/#key-stats
# 


import json

from . import caching



def get_url(url):
    try:
        response = caching.session.get(url)
        results = json.loads(response.text)
        return results

    except Exception as e:
        print("Error fetching data from server :- {}".format( url))
        print ("Response string:{}".format(response.text))
        return {}


def get_one_yr_change(ticker):
	base_url = "https://api.iextrading.com/1.0/stock/{}/stats?filter=year1ChangePercent"
	url = base_url.format(ticker)
	result = get_url(url)
	return result.get("year1ChangePercent", 0)

def get_one_yr_change_stocks(tickers_list):
	result = {}
	for ticker in tickers_list:
		result[ticker] = get_one_yr_change(ticker)
	return result


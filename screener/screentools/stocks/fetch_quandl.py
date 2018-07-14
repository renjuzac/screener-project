from ..config import quandl_api_key

from datetime import timedelta


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




def get_aq_multiple_stock(stock):

#	if len(stock) > 4 :
#		return 0

	ev_opinc_url = "https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker={}&dimension=MRY&&qopts.columns=ev,opinc&api_key={}"
	ev_opinc_url = ev_opinc_url.format(stock, quandl_api_key)
	results = get_url(ev_opinc_url)

	headers = []
	for entry in results["datatable"]["columns"]:
		headers.append(entry["name"])

	data = results["datatable"]["data"]
	if len(data) < 1:                      # Empty return for pink sheets
		return 0 
	else:
		data = data[-1]

	fundamentals = {}

	for headerv,datav in zip(headers, data):
		fundamentals[headerv] = datav
 

	try:
		result = round(fundamentals["ev"] /fundamentals["opinc"],2)
	except TypeError:
		result = 0

	return result 


def get_aq_multiple_stock_list(stocklist):
	# Columns returned are not guranteed to be in order , so fetch once ticker at a time
	ev_opinc_url = "https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker={}&dimension=MRY&&qopts.columns=ticker,ev,opinc&qopts.latest=1&api_key={}"

	aqmresult = {}
	stocklist_string = ""
	for stock in stocklist:
		stocklist_string = stocklist_string + "%2C" + stock


	ev_opinc_url_formatted = ev_opinc_url.format(stocklist_string, quandl_api_key)
	results = get_url(ev_opinc_url_formatted)

	values = results["datatable"]["data"]

	for value in values:
		try:
			ticker = value[0]
			ev = value[1]
			opinc = value[2]
		except IndexError:
			continue
		
		try:
			aqmresult[ticker] = round(ev/opinc, 2)   # ev /opinc
		except TypeError:
			aqmresult[stock] = 0

	return aqmresult 



def get_metadata(stock):
	ev_opinc_url = "https://www.quandl.com/api/v3/datatables/SHARADAR/TICKERS.json?ticker={}&qopts.columns=exchange,sicsector,sicindustry,famaindustry,scalerevenue&api_key={}"
	ev_opinc_url = ev_opinc_url.format(stock, quandl_api_key)
	results = get_url(ev_opinc_url)

	tabledata = results["datatable"]["data"] 
	tablecolumns = results["datatable"]["columns"] 

	res = {}

	for colname,data in zip(tablecolumns,tabledata[-1]):
		res[colname["name"]] = data

	return res



# FCF Debt AQM history 
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



def get_enterprise_multiple(stocklist):
	# https://www.investopedia.com/terms/e/ev-ebitda.asp
	evebitda_url = "https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker={}&dimension=MRQ&qopts.columns=ticker,evebitda&qopts.latest=1&api_key={}"
	aqmresult = {}
	stocklist_string = ""
	for stock in stocklist:
		stocklist_string = stocklist_string + "%2C" + stock


	evebitda_url_formatted = evebitda_url.format(stocklist_string, quandl_api_key)
	results = get_url(evebitda_url_formatted)

	values = results["datatable"]["data"]

	for value in values:
		try:
			ticker = value[0]
			evebitda = value[1]
		except IndexError:
			continue

		aqmresult[ticker] = evebitda

	return aqmresult 


def get_fundamental_value(stocklist,fundamentallist):
	fundamental_url = "https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker={}&dimension=MRQ&qopts.columns=ticker,{}&qopts.latest=1&api_key={}"
	funresult = {}
	stocklist_string = ""
	fundamentallist_string = ""
	for stock in stocklist:
		stocklist_string = stocklist_string + "%2C" + stock

	for fundamental in fundamentallist:
		fundamentallist_string = fundamentallist_string + "," + fundamental
	fundamentallist_string = fundamentallist_string.strip(",")


	fundamental_url_formatted = fundamental_url.format(stocklist_string, fundamentallist_string, quandl_api_key)

	print(fundamental_url_formatted)
	results = get_url(fundamental_url_formatted)

	print(results)

	values = results["datatable"]["data"]

	for value in values:
		try:
			ticker = value[0]
			fundamental_val = value[1:]
		except IndexError:
			continue

		funresult[ticker] = fundamental_val

	return funresult 


def get_debt_to_equity(stocklist):
	res = get_fundamental_value(stocklist,["debt","equity"])
	deres = {}
	for stock in res.keys():
		try:
			deres[stock] = round(res[stock][0] / res[stock][1] ,2)
		except(TypeError,ZeroDivisionError):
			deres[stock] = 0
	return deres





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
	except (TypeError,ZeroDivisionError):
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
		except (TypeError,ZeroDivisionError):
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


def get_revenue_growth(stocklist):
	revenue_url = "https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker={}&dimension=MRQ&qopts.columns=ticker,revenue&api_key={}"
	revresult ={}
	chunksize = 20        
	for i in range(0, len(stocklist), chunksize):
		symbolchunk = stocklist[i:i+chunksize]

		stocklist_string = ""

		for stock in symbolchunk:
			stocklist_string = stocklist_string + "%2C" + stock


		revenue_url_formatted = revenue_url.format(stocklist_string, quandl_api_key)
		print(symbolchunk,revenue_url_formatted)

		results = get_url(revenue_url_formatted)

		values = results["datatable"]["data"]

		current_ticker =""
		current_revenue_list = []

		for value in values:
			try:
				ticker = value[0]
				revenue = value[1]
				if not revenue:
					raise TypeError   # null revenue
				if current_ticker == "":
					current_ticker = ticker

				if current_ticker == ticker: 
					current_revenue_list.append(revenue)
				else:
					revresult[current_ticker] = round(((current_revenue_list[-1] - current_revenue_list[-5])*100) / current_revenue_list[-5],2)
					print("main",current_ticker,revresult[current_ticker])
					current_ticker = ticker
					current_revenue_list = []
					current_revenue_list.append(revenue)
			except (IndexError,ZeroDivisionError,TypeError):
				revresult[current_ticker] = 0
				current_ticker = ""  # zero revenue
				continue

		try:
			revresult[current_ticker] = round(((current_revenue_list[-1] - current_revenue_list[-5])*100) / current_revenue_list[-5],2)
			print(current_ticker,revresult[current_ticker])
		except (ZeroDivisionError,IndexError,TypeError):
			revresult[current_ticker] = 0

	print(revresult)
	return revresult




# FCF , Debt , AQM  history , revenue growth history  
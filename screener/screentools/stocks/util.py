import datetime
import pytz


from reports.models import Report, Scan, Stock
from screentools.stocks import scan
from screentools.stocks import fetch
from screentools.stocks import screendata


def is_update_required(last_updated_at):

	utc_now = pytz.utc.localize(datetime.datetime.utcnow())
	pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))

	today = datetime.date.today ()
	afternoon3pm = datetime.time(hour=15, minute=00)
	today3pm = datetime.datetime.combine(today, afternoon3pm,pytz.timezone("America/Los_Angeles"))

	yesterday = datetime.date.today () - datetime.timedelta (days= 1)
	yesterday3pm = datetime.datetime.combine(yesterday, afternoon3pm,pytz.timezone("America/Los_Angeles"))

	# print(today3pm)
	# print(report.last_update -pst_now)




	if today.weekday() < 6 :   # Monday - Friday
		try:
			if last_updated_at < today3pm and pst_now > today3pm:  # was last updated earlier than 3pm today 
				return True
			if last_updated_at < yesterday3pm and pst_now < today3pm: #wasnt updated yesterday
				return True
		except TypeError:
			return True

	if today.weekday() in [6,7] :   # Saturday - Sunday 
		last_friday = datetime.date.today () - datetime.timedelta (days= today.weekday() -5)
		friday3pm = datetime.datetime.combine(last_friday, afternoon3pm,pytz.timezone("America/Los_Angeles"))
		try:
			if last_updated_at < friday3pm:
				return True
		except TypeError:
			return True

	return False

# https://stackoverflow.com/questions/23642676/python-set-datetime-hour-to-be-a-specific-time
# https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python


def meets_min_stock_criteria(stock):
	'''
	Close > $10
	Volume > 1M
	'''
	try: 
		return (stock['close'] > 10 and stock['avgVolume'] > 750000)
	except TypeError:
		return False

def update_stock(symbol,entry=None , aqm=None, rev=None):
		print("updating" , symbol)
		if not entry:
			entry  = fetch.getquote(symbols=[symbol])[0]
		stock, created = Stock.objects.get_or_create(symbol=symbol)
		stock.name = entry['name']
		try:
			stock.fiftyTwoWkHigh = round((entry['fiftyTwoWkHigh'] - entry['close'])*100 / entry['close'],2) # save as percentage
			stock.fiftyTwoWkLow = round((entry['close'] - entry['fiftyTwoWkLow'])*100 / entry['close'],2)
		except ZeroDivisionError:
			stock.fiftyTwoWkHigh = 0
			stock.fiftyTwoWkLow = 0


		stock.avgVolume = entry['avgVolume']
		stock.twentyDayAvgVol = entry['twentyDayAvgVol']
		stock.exchange = entry['exchange']
		stock.lastPrice = entry['lastPrice']
		stock.netChange = entry['netChange']
		stock.percentChange = entry['percentChange']
		stock.open_price = entry['open']
		stock.high_price = entry['high']
		stock.low_price = entry['low']
		stock.close_price = entry['close']
		stock.volume = entry['volume']
		try:
			if aqm:
				stock.aquirersMultiple = aqm[symbol]
			else:
			#stock.aquirersMultiple = fetch.get_aq_multiple_stock(symbol)
				stock.aquirersMultiple = fetch.get_enterprise_multiple([symbol])[symbol]
		except KeyError:
				stock.aquirersMultiple = 0

		try:
			if rev and rev[symbol]:
				stock.revenue_growth = rev[symbol]
			else:
				stock.revenue_growth = fetch.get_revenue_growth([symbol])[symbol]
		except (KeyError,TypeError) as e:
			stock.revenue_growth = 0

		stock.one_yr_change = round(fetch.get_one_yr_change(symbol)*100 ,2)

		utc_now = pytz.utc.localize(datetime.datetime.utcnow())
		pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
		stock.last_update = pst_now
		stock.save()

		return stock



def update_report(report_id):
	report = Report.objects.filter(id__exact=report_id).get()
	scannerfn = report.factor.function      # Function name stored in model

#	function=getattr(scan,scannerfn) 
	function=getattr(screendata,scannerfn)  # Get the function

	stocks_list = function()     # Call the function 

#	aqm_values = fetch.get_aq_multiple_stock_list(stocks_list)
	aqm_values = fetch.get_enterprise_multiple(stocks_list)

	if report.is_a_value_scan:

		value_stocks_list = []

		for stock in stocks_list:
			try:
				if aqm_values[stock] > 0 and aqm_values[stock] < 30:    # pick aqm less than 30 
					value_stocks_list.append(stock) 
			except (KeyError,TypeError):
				continue

		stocks_list = value_stocks_list

	revenue_growth = fetch.get_revenue_growth(stocks_list)

#	growth_stocks_list = scan.scan_on_growth()
	stock_quotes  = fetch.getquote(symbols=stocks_list)
	for entry in stock_quotes:
		if meets_min_stock_criteria(entry):
			stock = update_stock(symbol=entry['symbol'],entry=entry , aqm = aqm_values, rev = revenue_growth)
			report.stocks.add(stock)

			utc_now = pytz.utc.localize(datetime.datetime.utcnow())
			pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
			report.last_update = pst_now
			report.save()

# https://djangobook.com/django-models-basic-data-access/
# https://stackoverflow.com/questions/4075190/what-is-getattr-exactly-and-how-do-i-use-it
# https://ubuntuforums.org/showthread.php?t=1110989
# https://ubuntuforums.org/showthread.php?t=1110989
# https://stackoverflow.com/questions/4075190/what-is-getattr-exactly-and-how-do-i-use-it


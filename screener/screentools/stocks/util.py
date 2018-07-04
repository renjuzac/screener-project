import datetime
import pytz


from reports.models import Report, Scan, Stock
from screentools.stocks import scan
from screentools.stocks import fetch


def is_update_required(last_updated_at):

	utc_now = pytz.utc.localize(datetime.datetime.utcnow())
	pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))

	today = datetime.date.today ()
	afternoon3pm = datetime.time(hour=15, minute=00)
	today3pm = datetime.datetime.combine(today, afternoon3pm,pytz.timezone("America/Los_Angeles"))

	# print(today3pm)
	# print(report.last_update -pst_now)



	if today.weekday() < 6 :   # Monday - Friday
		if last_updated_at < today3pm:
			return True

	if today.weekday() in [6,7] :   # Saturday - Sunday 
		last_friday = datetime.date.today () - datetime.timedelta (days= today.weekday() -5)
		friday3pm = datetime.datetime.combine(last_friday, afternoon3pm,pytz.timezone("America/Los_Angeles"))
		if last_updated_at < friday3pm:
			return True

	return False

# https://stackoverflow.com/questions/23642676/python-set-datetime-hour-to-be-a-specific-time
# https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python


def update_report(report_id):
	report = Report.objects.filter(id__exact=report_id).get()
	scanner = report.factor.function

	growth_stocks_list = scan.scan_on_growth()
	stock_quotes  = fetch.getquote(symbols=growth_stocks_list)

	for entry in stock_quotes:
		stock, created = Stock.objects.get_or_create(symbol=entry['symbol'])
		stock.name = entry['name']
		stock.fiftyTwoWkHigh = round((entry['fiftyTwoWkHigh'] - entry['close'])*100 / entry['close'],2) # save as percentage
		stock.fiftyTwoWkLow = round((entry['close'] - entry['fiftyTwoWkLow'])*100 / entry['close'],2)
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

		stock.save()
		report.stocks.add(stock)

		utc_now = pytz.utc.localize(datetime.datetime.utcnow())
		pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
		report.last_update = pst_now
		report.save()

# https://djangobook.com/django-models-basic-data-access/
# https://stackoverflow.com/questions/4075190/what-is-getattr-exactly-and-how-do-i-use-it
# https://ubuntuforums.org/showthread.php?t=1110989


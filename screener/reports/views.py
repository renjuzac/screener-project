import json

from rq import Queue       # Heroku background processing
from worker import conn    # Heroku background processing

from django.shortcuts import render
from django.shortcuts import redirect
from .models import Report, Scan, Stock
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist

from django_tables2 import RequestConfig
from .tables import ReportDetailTable

from screentools.stocks import scan
from screentools.stocks import util
from screentools.stocks import fetch




stocks = scan.scan_on_growth()



# Create your views here.


def index(request):
	reports = Report.objects.all()
	stocks = scan.scan_on_growth()
	return render(request, "index.html" ,context = {"reports":reports})


def report_detail(request, id=1):
	report = Report.objects.filter(id__exact=id).get()


	if util.is_update_required(report.last_update):
		q = Queue(connection=conn)
		print(q)
		result = q.enqueue(util.update_report, id)   # https://devcenter.heroku.com/articles/python-rq
		print(result)
		# util.update_report(report_id= id)        # Blocking call 
		return redirect('updating')


	response = dict()
	response['name'] = report.name
	response['factor'] = ""
	response['last_update'] = report.last_update
	table = ReportDetailTable(report.stocks.values())
	RequestConfig(request).configure(table)
	response['stocks'] = table


	return render(request, "report-detail.html" ,context = {"report_detail":response})

def stock_detail(request, symbol):
	try:
		stock = Stock.objects.filter(symbol__iexact=symbol).get()
		if util.is_update_required(stock.last_update):
			util.update_stock(symbol=symbol)
			stock = Stock.objects.filter(symbol__iexact=symbol).get()
	except ObjectDoesNotExist:
		util.update_stock(symbol=symbol)
		stock = Stock.objects.filter(symbol__iexact=symbol).get()
	response = serialize('json', [stock])
	response = json.loads(response)[0]['fields']
	stock_meta = fetch.get_metadata(symbol)
	response.update(stock_meta)
	return render(request, "stock.html" ,context = {"price_data":response})


def auto_report(request, type):
	response = dict()

	if str.lower(type) == "value":
		stocks = Stock.objects.filter(aquirersMultiple__lte=20).filter(revenue_growth__gte=15).filter(one_yr_change__gte=25).filter(aquirersMultiple__gte=0)
		response['name'] = "Value Stocks - Auto Generated"
	else:
		stocks = Stock.objects.filter(revenue_growth__gte=25).filter(one_yr_change__gte=25)
		response['name'] = "Growth Stocks - Auto Generated"

	table = ReportDetailTable(stocks.values())
	RequestConfig(request).configure(table)
	response['stocks'] = table

	return render(request, "report-detail.html" ,context = {"report_detail":response})

def clean(request):
	Stock.objects.filter(revenue_growth__lte=10).delete()  # Low growth
	Stock.objects.filter(one_yr_change__lte=5).delete()  # Non trending
	Stock.objects.filter(aquirersMultiple__iexact=0).delete()  # No aquirers multiple data
	return redirect('index')

def updating(request):
	return render(request, "updating.html", context = {})




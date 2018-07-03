import json

from django.shortcuts import render
from .models import Report, Scan, Stock
from django.core.serializers import serialize


from screentools.stocks import scan
from screentools.stocks import util


stocks = scan.scan_on_growth()



# Create your views here.


def index(request):
	reports = Report.objects.all()
	stocks = scan.scan_on_growth()
	print(stocks)
	return render(request, "index.html" ,context = {"reports":reports})


def report_detail(request, id=1):
	report = Report.objects.filter(id__exact=id).get()

	if util.is_update_required(report.last_update):
		util.update_report("name",report_id= id)


	response = {}
	response['name'] = report.name
	response['factor'] = ""
	response['stocks'] = report.stocks.values()
	response['last_update'] = report.last_update

	return render(request, "report-detail.html" ,context = {"report_detail":response})

def stock_detail(request, symbol):
	response = serialize('json', [Stock.objects.filter(symbol__icontains=symbol).get()])
	response = json.loads(response)[0]['fields']
	return render(request, "stock.html" ,context = {"price_data":response})


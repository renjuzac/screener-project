from django.shortcuts import render
from .models import Report, Scan, Stock
from django.core.serializers import serialize
import json



# Create your views here.


def index(request):
	reports = Report.objects.all()
	return render(request, "index.html" ,context = {"reports":reports})


def report_detail(request, id=1):
	response = {}
	report = Report.objects.filter(id__exact=id).get()
	response['name'] = report.name
	response['factor'] = ""
	response['stocks'] = report.stocks.values()
	response['last_update'] = report.last_update
	return render(request, "report-detail.html" ,context = {"report_detail":response})

def stock_detail(request, symbol):
	response = serialize('json', [Stock.objects.filter(symbol__icontains=symbol).get()])
	response = json.loads(response)[0]['fields']
	return render(request, "stock.html" ,context = {"price_data":response})


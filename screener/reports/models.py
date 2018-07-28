from django.db import models
from django.urls import reverse

# Create your models here.

class Stock(models.Model):
	symbol = models.CharField(max_length=20, unique=True)
	name = models.CharField(max_length=50,null=True, blank=True)
	fiftyTwoWkLow = models.FloatField(null=True, blank=True)
	fiftyTwoWkHigh = models.FloatField(null=True, blank=True)
	avgVolume = models.FloatField(null=True, blank=True)
	aquirersMultiple = models.FloatField(null=True, blank=True)
	one_yr_change = models.FloatField(null=True, blank=True)
	revenue_growth = models.FloatField(null=True, blank=True)
	composite_Metric = models.FloatField(null=True, blank=True)
	close_price = models.FloatField(null=True, blank=True)
	twentyDayAvgVol = models.FloatField(null=True, blank=True)
	exchange = models.CharField(max_length=20,null=True, blank=True)	
	lastPrice = models.FloatField(null=True, blank=True)
	netChange = models.FloatField(null=True, blank=True)
	percentChange = models.FloatField(null=True, blank=True)
	open_price = models.FloatField(null=True, blank=True)
	high_price = models.FloatField(null=True, blank=True)
	low_price = models.FloatField(null=True, blank=True)
	volume = models.IntegerField(null=True, blank=True)
	last_update = models.DateTimeField(null=True)



	def get_absolute_url(self):
		return reverse('stock_detail', args=[str(self.symbol)])

	def __str__(self):
		return '{}'.format(self.symbol)


class Report(models.Model):
	name = models.CharField(max_length=20, help_text="Report Name")
	factor = models.ForeignKey('Scan', on_delete=models.SET_NULL, null=True)  # Foreign key scan 
	stocks = models.ManyToManyField(Stock, blank=True)  # Stock tickers
	last_update = models.DateTimeField()
	is_a_value_scan = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('report-detail', args=[str(self.id)])

	def __str__(self):
		return '{}'.format(self.name)


class Scan(models.Model):
	name = models.CharField(max_length=20, help_text="Scan Name")
	description = models.CharField(max_length=50, help_text="scanner description")  
	function = models.CharField(max_length=50,null=True, blank=True, help_text="scanner function") # A function that holds scan critria 

	def __str__(self):
		return '{}'.format(self.name)


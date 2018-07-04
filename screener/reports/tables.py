import django_tables2 as tables
from .models import Report, Scan, Stock
from django.urls import reverse
from django.utils.safestring import mark_safe


class ReportDetailTable(tables.Table):
	symbol = tables.Column()

	def render_symbol(self,value):
		
		stock_url = reverse("stock_detail", args=[value])
		return mark_safe('''<a href="%s" class="tbl_icon edit">%s</a>''' % (stock_url, value))

	class Meta:
		model = Stock
		sequence = ('symbol', 'close_price','avgVolume','netChange', 'percentChange','fiftyTwoWkHigh','fiftyTwoWkLow','name')
		exclude = ('id','open_price','high_price','low_price','twentyDayAvgVol ' )
		template_name = 'django_tables2/bootstrap.html'




# https://stackoverflow.com/questions/6275193/django-tables2-linkcolumn-multiple-items-in-the-same-cell/6275332#6275332
# http://andrewtremblay.com/articles/thousands-separator-in-django-tables2/

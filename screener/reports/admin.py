from django.contrib import admin
from .models import Stock, Report, Scan

# Register your models here.

admin.site.register(Stock)
admin.site.register(Report)
admin.site.register(Scan)


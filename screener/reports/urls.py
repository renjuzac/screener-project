from django.urls import path
from . import views


urlpatterns = [
				path('',views.index, name="index"),
				path('report-detail/<int:id>/',views.report_detail, name="report_detail"),
				path('stock-detail/<str:symbol>/',views.stock_detail, name="stock_detail")

				]
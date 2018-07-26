from django.urls import path
from . import views


urlpatterns = [
				path('',views.index, name="index"),
				path('report-detail/<int:id>/',views.report_detail, name="report_detail"),
				path('stock-detail/<str:symbol>/',views.stock_detail, name="stock_detail"),
				path('auto-report/<str:type>/',views.auto_report, name="auto_report"),
				path('clean',views.clean, name="clean"),
				path('updating',views.updating, name="updating")

				]
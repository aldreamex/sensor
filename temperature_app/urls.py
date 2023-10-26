from django.contrib import admin
from django.urls import path, include
from temperature_app.views import temperature_chart, chart_update_data

urlpatterns = [
    path('', temperature_chart, name='temperature_chart'),
    path('chart_update_data/', chart_update_data, name='chart_update_data'),
]
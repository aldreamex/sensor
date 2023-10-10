from django.contrib import admin
from django.urls import path, include
from temperature_app.views import temperature_chart, chart_update

urlpatterns = [
    path('chart/', temperature_chart, name='temperature_chart'),
    path('chart_update/', chart_update, name='chart_update'),
]
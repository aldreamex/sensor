from django.contrib import admin
from django.urls import path, include
from temperature_app.views import temperature_chart

urlpatterns = [
    path('chart/', temperature_chart, name='temperature_chart'),
]
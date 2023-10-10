import json
from django.http import JsonResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import TemperatureReading
import pytz
from .utils import create_chart


def temperature_chart(request):
    # Получаем последние 5 записей изменения температуры из БД
    readings = TemperatureReading.objects.order_by('-timestamp')[:5]
    chart_data = create_chart(readings)


    context = {
        'chart_data': chart_data
    }

    return render(request, 'temperature_chart.html', context)


 # Еще один совет, функцию которая будет график тебе создавать вынеси отдельно от views  к примеру создай файл utils  и туда положи
def chart_update(request):
    readings = TemperatureReading.objects.order_by('-timestamp')[:5]
    chart_data = create_chart(readings)
    #json_data = json.dumps({'chart_data':chart_data}) - у тебя было так эта штука тож  json возвращает

    return JsonResponse({'chart_data':chart_data}, safe=False)

# крч надо вынести функционал создания графика в отдельную функцию, т.к. он у нас уже переиспользуется
# потом в новой view это все заюзать и вернуть в виде  json
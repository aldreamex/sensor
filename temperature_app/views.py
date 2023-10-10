from django.http import JsonResponse
from django.shortcuts import render
from .models import TemperatureReading
from .utils import create_chart

def temperature_chart(request):
    """Отображение графика температур"""

    readings = TemperatureReading.objects.order_by('-timestamp')[:5]
    chart_data = create_chart(readings)

    context = {
        'chart_data': chart_data
    }

    return render(request, 'temperature_chart.html', context)


def chart_update_data(request):
    """Обновление данных на графике"""

    readings = TemperatureReading.objects.order_by('-timestamp')[:5]
    chart_data = create_chart(readings)

    context = {
        'chart_data': chart_data
    }

    return JsonResponse(context, safe=False)

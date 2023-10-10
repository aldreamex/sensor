from django.http import JsonResponse
from django.shortcuts import render
from .models import TemperatureReading
from .utils import create_chart

def temperature_chart(request):
    # Получаем последние 5 записей изменения температуры из БД
    readings = TemperatureReading.objects.order_by('-timestamp')[:5]
    chart_data = create_chart(readings)

    context = {
        'chart_data': chart_data
    }

    return render(request, 'temperature_chart.html', context)


def chart_update_data(request):
    readings = TemperatureReading.objects.order_by('-timestamp')[:5]
    chart_data = create_chart(readings)
    #json_data = json.dumps({'chart_data':chart_data})

    return JsonResponse({'chart_data':chart_data}, safe=False)

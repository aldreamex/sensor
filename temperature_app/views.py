from django.http import JsonResponse
from django.shortcuts import render
from .models import TemperatureReading
from .utils import create_chart
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def sensor_data(request):
    """Приемка данных от датчика и сохранение в БД"""

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            temperature = data.get('t')

            reading = TemperatureReading.objects.create(
                temperature=temperature
            )

            return JsonResponse({'message': 'Данные успешно сохранены'}, status=200)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Неверный формат данных'}, status=400)

    else:
        return JsonResponse({'error': 'Метод не поддерживается'}, status=405)


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

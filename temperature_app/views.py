import matplotlib
matplotlib.use('Agg')  # Agg для рендеринга графика
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import TemperatureReading
import pytz


def temperature_chart(request):
    # Последние 5 записей изменения температуры
    readings = TemperatureReading.objects.order_by('-timestamp')[:5]


    timezone = pytz.timezone('Europe/Moscow')
    timestamps = [reading.timestamp.astimezone(timezone).strftime("%Y-%m-%d %H:%M:%S") for reading in readings]

    temperatures = [reading.temperature for reading in readings]

    # Стиль графика
    plt.style.use('classic')

    # График
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(timestamps, temperatures, marker='o', linestyle='-', color='b', label='Температура')
    ax.set_xlabel('Дата/время')
    ax.set_ylabel('Температура (°C)')
    ax.set_title('График показаний температуры с датчика')
    ax.grid(True)
    ax.legend()

    # Сохраняем график в памяти
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Преобразуем изображение в строку
    chart_data = base64.b64encode(buffer.read()).decode()
    buffer.close()

    context = {
        'chart_data': chart_data
    }
    return render(request, 'temperature_chart.html', context)

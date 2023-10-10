import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import TemperatureReading
import pytz
matplotlib.use('Agg')

def create_chart(readings):
    """Функция построения графика"""

    timezone = pytz.timezone('Europe/Moscow')
    timestamps = [reading.timestamp.astimezone(timezone).strftime("%Y-%m-%d %H:%M:%S") for reading in readings]
    temperatures = [reading.temperature for reading in readings]

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(timestamps, temperatures, marker='o', linestyle='-', color='b', label='Температура')
    ax.set_xlabel('Дата/время')
    ax.set_ylabel('Температура (°C)')
    ax.set_title('График показаний температуры с датчика')
    ax.grid(True)
    ax.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    chart_data = base64.b64encode(buffer.read()).decode()
    buffer.close()

    return chart_data
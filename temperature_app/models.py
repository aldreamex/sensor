from django.db import models


class TemperatureReading(models.Model):
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    mac_address = models.CharField(max_length=17, default="", null=True)



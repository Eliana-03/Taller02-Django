from django.db import models
from measurements.models import Measurement

class Alarm(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.ManyToManyField(Measurement)
    def __str__(self) -> str:
        return '{}'.format(self.name)
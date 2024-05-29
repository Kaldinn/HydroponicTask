from django.db import models
from django.contrib.auth.models import User

class HydroponicSystem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Measurement(models.Model):
    hydroponic_system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ph = models.FloatField()
    temperature = models.FloatField()
    tds = models.IntegerField()

    def __str__(self):
        return f"{self.hydroponic_system.name} - {self.timestamp}"
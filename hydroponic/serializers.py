from rest_framework import serializers
from .models import HydroponicSystem, Measurement

class HydroponicSystemSerializer(serializers.Serializer):
    class Meta:
        model = HydroponicSystem
        fields = ['id', 'name', 'description', 'owner']

class MeasurementSerializer(serializers.Serializer):
    class Meta:
        model = Measurement
        fields = ['id', 'hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds']
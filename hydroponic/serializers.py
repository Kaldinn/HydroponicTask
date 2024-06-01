from rest_framework import serializers
from .models import HydroponicSystem, Measurement

class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ['id', 'name', 'description', 'owner']

    def validate_name(self, value):
        if 'forbidden' in value.lower():
            raise serializers.ValidationError("Name cannot contain the word 'forbidden'")
        return value
        
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds']

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)

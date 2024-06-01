from rest_framework import serializers
from .models import HydroponicSystem, Measurement

class HydroponicSystemSerializer(serializers.ModelSerializer):
    """
        Serializer for HydroponicSystem model
        Includes validation for the name field
    """
    class Meta:
        model = HydroponicSystem
        fields = ['id', 'name', 'description', 'owner']

    def validate_name(self, value):
        """
            Check that the name does not contain the word 'forbidden'
        """
        if 'forbidden' in value.lower():
            raise serializers.ValidationError("Name cannot contain the word 'forbidden'")
        return value
        
class MeasurementSerializer(serializers.ModelSerializer):
    """
        Serializer for Measurement model
    """
    class Meta:
        model = Measurement
        fields = ['id', 'hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds']

    def create(self, validated_data):
        """
            Create and return a new Measurement instance, given the validated data
        """
        return Measurement.objects.create(**validated_data)

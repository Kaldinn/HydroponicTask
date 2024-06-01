from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer

class HydroponicSystemList(ListCreateAPIView):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'description', 'owner']
    ordering_fields = ['name', 'description', 'owner']
    ordering = ['name']

class HydroponicSystemDetail(RetrieveUpdateDestroyAPIView):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

class MeasurementList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds']
    ordering_fields = ['timestamp', 'ph', 'temperature', 'tds']
    ordering = ['timestamp']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MeasurementDetail(RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

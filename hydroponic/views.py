from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer


class HydroponicSystemList(ListCreateAPIView):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'description', 'owner']
    ordering_fields = ['name', 'description', 'owner']
    ordering = ['name']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HydroponicSystemDetail(RetrieveUpdateDestroyAPIView):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

class MeasurementList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds']
    ordering_fields = ['timestamp', 'ph', 'temperature', 'tds']
    ordering = ['timestamp']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Measurement.objects.filter(hydroponic_system__owner=self.request.user)

    def perform_create(self, serializer):
        hydroponic_system = HydroponicSystem.objects.get(id=self.request.data['hydroponic_system'], owner=self.request.user)
        serializer.save(hydroponic_system=hydroponic_system)
        
class MeasurementDetail(RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Measurement.objects.filter(hydroponic_system__owner=self.request.user)

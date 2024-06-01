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
    """
        API view to retrieve list of hydroponic systems or create new
        Allows filtering and ordering of results
    """
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'description', 'owner']
    ordering_fields = ['name', 'description', 'owner']
    ordering = ['name']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            Filter hydroponic systems by the current user
        """
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
            Set the owner of the hydroponic system to the current user
        """
        serializer.save(owner=self.request.user)

class HydroponicSystemDetail(RetrieveUpdateDestroyAPIView):
    """
        API view to retrieve, update or delete hydroponic system
    """
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            Filter hydroponic systems by the current user
        """
        return HydroponicSystem.objects.filter(owner=self.request.user)

class MeasurementList(ListCreateAPIView):
    """
        API view to retrieve list of measurements or create new
        Allows filtering and ordering of results
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds']
    ordering_fields = ['timestamp', 'ph', 'temperature', 'tds']
    ordering = ['timestamp']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            Filter measurements by hydroponic systems owned by the current user
        """
        return Measurement.objects.filter(hydroponic_system__owner=self.request.user)

    def perform_create(self, serializer):
        """
            Create a new measurement and assign it to the hydroponic system
        """
        hydroponic_system = HydroponicSystem.objects.get(id=self.request.data['hydroponic_system'], owner=self.request.user)
        serializer.save(hydroponic_system=hydroponic_system)
        
class MeasurementDetail(RetrieveUpdateDestroyAPIView):
    """
        API view to retrieve, update or delete a measurement
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            Filter measurements by hydroponic systems owned by the current user
        """
        return Measurement.objects.filter(hydroponic_system__owner=self.request.user)

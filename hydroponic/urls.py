from django.urls import path
from .views import HydroponicSystemList, MeasurementList, Measurement

urlpatterns = [
    path(
        'hydroponic_system/',
        HydroponicSystemList.as_view(),
        name="hydroponic_system"),
    path(
        'measurement_system',
        MeasurementList.as_view(),
        name="measurement_system"),
    path(
        'measurement/<int:pk>/',
        Measurement.as_view(),
        name="measurement"
    )
]
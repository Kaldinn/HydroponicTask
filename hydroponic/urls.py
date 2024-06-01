from django.urls import path
from .views import HydroponicSystemList, HydroponicSystemDetail, MeasurementList, MeasurementDetail

urlpatterns = [
    path('hydroponic_system/', HydroponicSystemList.as_view(), name="hydroponic_system"),
    path('hydroponic_system/<int:pk>/', HydroponicSystemDetail.as_view(), name='hydroponic_system_detail'),
    path('measurement/', MeasurementList.as_view(), name="measurement"),
    path('measurement/<int:pk>/', MeasurementDetail.as_view(), name="measurement_pk"),
]

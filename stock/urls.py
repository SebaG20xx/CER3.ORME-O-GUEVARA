
from django.urls import include,path

from .views import VehiculoAPIView, VehiculoDetailAPIView

urlpatterns = [
    path('vehiculos/', VehiculoAPIView.as_view(), name='vehiculo-list'),
    path('vehiculos/<int:pk>/', VehiculoDetailAPIView.as_view(), name='vehiculo-detail'),
]

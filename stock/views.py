from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Vehiculo
from .serializers import VehiculoSerializer


class VehiculoAPIView(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
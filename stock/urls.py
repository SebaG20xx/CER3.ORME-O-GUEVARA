from stock.views import VehiculoList

urlpatterns = [
    path('vehiculos/', VehiculoList.as_view(), name='vehiculo-list'),
    # Agrega otras rutas de URL para tus vistas de la API REST
]
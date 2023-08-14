from django.urls import path
from . import codigop, llave
from . import views
#aqui hay rutas desde la raiz
urlpatterns = [
    path("", views.index, name="index"),
    path("validacion", llave.Keycdmx, name='validacion'),
]
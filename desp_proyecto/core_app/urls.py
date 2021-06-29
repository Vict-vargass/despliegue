from django.urls import path
from .views import home, inicio_real
urlpatterns = [
    path('', home, name="home"),
    path('inicio', inicio_real, name="inicio")
    ]
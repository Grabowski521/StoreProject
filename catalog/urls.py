from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Базовый маршрут для приложения
]
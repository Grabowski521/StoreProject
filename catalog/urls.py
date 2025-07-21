from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),         # Главная страница
    path('contacts/', views.contacts, name='contacts'),  # Страница контактов
    path('categories/', views.categories_view, name='categories'),
    path('orders/', views.orders_view, name='orders'),
]
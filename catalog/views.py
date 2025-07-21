from django.shortcuts import render
from .models import Category
#from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')  # Главная страница

def contacts(request):
    return render(request, 'contacts.html')  # Страница контактов

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'catalog/categories.html', {'categories': categories})

def orders_view(request):
    categories = Category.objects.all()
    return render(request, 'catalog/orders.html', {'categories': categories})
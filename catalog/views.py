from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')  # Главная страница

def contacts(request):
    return render(request, 'contacts.html')  # Страница контактов
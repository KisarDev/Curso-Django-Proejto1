from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Cesar Augusto'})


def contato(request):
    return HttpResponse('<h1>contato<h1>')


def checkout(request):
    return HttpResponse('<h1>checkout<h1>')


def carrinho(request):
    return HttpResponse('<h1>carrinho-Home<h1>')

from django.urls import path

from recipes.views import carrinho, checkout, contato, home

urlpatterns = [
    path('contato/', contato),
    path('', home),
    path('carrinho/', carrinho),
    path('carrinho/checkout', checkout),
]

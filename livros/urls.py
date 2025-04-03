from django.urls import path
from .views import listar_livros,api_livros

urlpatterns = [
    path('', listar_livros, name='listar_livros'),
    path('api/livros/', api_livros, name='api_livros'),
]

from django.shortcuts import render
from .models import Livro

def listar_livros(request):
    #o que ele vai listar
    livros = Livro.objects.all()  # Buscar todos os livros do banco de dados
    return render(request, 'livros.html', {'livros': livros})
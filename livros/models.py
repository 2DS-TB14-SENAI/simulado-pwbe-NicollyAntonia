from django.db import models
import random
def default_paginas():
    return random.randint(0, 1000000)  # Retorna um número aleatório entre 100 e 1000

class Livro (models.Model):
    titulo= models.CharField(max_length=50)
    autor= models.CharField(max_length=30)
    paginas= models.IntegerField(default=default_paginas)
    
    def __str__(self):
        return self.titulo

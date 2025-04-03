from django.apps import AppConfig

class LivrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'livros'  # Certifique-se de que está 'livros', e não 'applivro'

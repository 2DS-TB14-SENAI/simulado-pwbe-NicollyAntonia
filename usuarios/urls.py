from django.urls import path
from . import views

urlpatterns  = [
    path('auth/registro/', views.criar_Usuario),
    path('auth/login/', views.logar),

]
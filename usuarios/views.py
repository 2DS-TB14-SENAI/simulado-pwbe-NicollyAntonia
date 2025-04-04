from django.shortcuts import render 
from .models import UserAbs
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from .serializer import UsersSerializer

@api_view
def criar_Usuario(request):
    fone = request.data.get('fone')
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not all ([fone,username,password]):
        return Response ({'error':'informações insuficientes para cirar usuario'}, status=status.HTTP_400_BAD_REQUEST)
    if UserAbs.objects.filter(fone==fone).exists():
        return Response({'errors':'Já possui um usuario com este telefone cadastrado'}, status=status.HTTP_400_BAD_REQUEST)
    if UserAbs.objects.filter(username==username).exists():
        return Response({'errors':'Já possui um usuario com este nome cadastrado'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario= UserAbs.objects.criar_Usuario(
            fone=fone,
            username= username,
            password = password,
        )
        return Response({'Mensagem': 'User criado com sucesso'}, status=status.HTTP_201_CREATED)     
    except Exception as e:
        return Response({'error': f'Erro ao criar usuário: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['POST'])
def logar(request):
    fone =request.data.get('fone')
    username = request.data.get('username')
    password =request.data.get('password')
    
    if not username or not password or not fone :
        return Response({'Erro' : 'Informações insuficientes para fazer o login'}, status= status.HTTP_200_OK)
    
    user = authenticate(username = username , password = password, fone = fone)

    if user :
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    return Response({'Acesso negado'}, status= status.HTTP_401_UNAUTHORIZED)
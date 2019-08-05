from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Demanda,Endereco,Peca,Contato,Anunciante
from .serializers import DemandaSerializer,PecaSerializer,EnderecoSerializer,AnuncianteSerializer,ContatoSerializer


class DemandaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer

class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class AnuncianteViewSet(viewsets.ModelViewSet):
    queryset = Anunciante.objects.all()
    serializer_class = AnuncianteSerializer    

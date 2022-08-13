from rest_framework import viewsets
from Relatorio.models import Receita, Dispesa
from Relatorio.serializer import ReceitaSerializer, DispesaSerializer

class ReceitasViewSet(viewsets.ModelViewSet):
    '''Exibindo Receitas'''
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class DispesaViewSet(viewsets.ModelViewSet):
    '''Exibindo Dispesas'''
    queryset = Dispesa.objects.all()
    serializer_class = DispesaSerializer

from dataclasses import fields
from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from Relatorio.models import Receita, Dispesa

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id', 'descricao', 'valor', 'data']

class DispesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispesa
        fields = '__all__'

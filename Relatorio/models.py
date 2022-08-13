from enum import unique
from django.db import models


class Receita(models.Model):
    descricao = (models.CharField(max_length=100))
    valor = (models.FloatField(max_length=10))
    data = models.DateField(unique= True)
    #total_receita = print('Total = ',salario:.02f + renda_Extra:.02f)


    def __str__(self):
        return self.descricao


class Dispesa(models.Model):
    descricao = (models.CharField(max_length=10))
    valor = (models.FloatField(max_length= 10))
    data = models.DateField()


    def __str__(self):
        return self.descricao



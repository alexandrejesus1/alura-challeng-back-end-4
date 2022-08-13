from django.contrib import admin
from Relatorio.models import Receita, Dispesa

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 10


admin.site.register(Receita, Receitas)


class Dispesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 10

admin.site.register(Dispesa, Dispesas)

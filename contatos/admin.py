from django.contrib import admin

from . import models


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','data_criacao','mostrar')

    list_display_links = ['id','nome','sobrenome']

    list_filter = ['categoria']

    list_per_page = 2

    search_fields = ['nome','sobrenome','email','telefone']

    list_editable = ['mostrar']



admin.site.register(models.Contato,ContatoAdmin)
admin.site.register(models.Categoria)

# Register your models here.

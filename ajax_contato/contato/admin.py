# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['assunto',]
    search_fields = ['assunto',]

admin.site.register(Contato, ContatoAdmin)

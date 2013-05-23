# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

#from .forms import EmailUsuarioChangeForm, EmailUsuarioCreationForm
from .models import Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['assunto',]
    search_fields = ['assunto',]

admin.site.register(Contato, ContatoAdmin)
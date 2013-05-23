from django import forms
from .models import Contato
from .utils import AjaxBaseForm, AjaxForm, AjaxModelForm

class ContatoForm(AjaxModelForm):
	class Meta:
		model = Contato
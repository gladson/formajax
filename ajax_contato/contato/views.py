# -*- coding: utf-8 -*-
#from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContatoForm

try:
    import json
except ImportError:
    try:
        import simplejson
    except ImportError:
        from django.utils import simplejson


def contato(request):
	if request.method == 'GET':
		form = ContatoForm()
	else:
		form = ContatoForm(request.POST)
		if form.is_valid():
			salvando_contato = form.save(commit=False)
			salvando_contato.save()
			response = {'success' : True}
		else:
			response = form.errors_as_json()
			return HttpResponse(json.dumps(response, ensure_ascii=False),
                mimetype='application/json')
	return render(request, 'contato/contato.html', {'form': form})
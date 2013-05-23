from django.conf.urls.defaults import *
from django.conf import settings

from .views import contato

urlpatterns = patterns('',
	url(r'^ajax_contato/$', 'contato.views.contato', name='contato'),
)
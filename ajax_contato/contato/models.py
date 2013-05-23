# -*- coding: utf-8 -*-
from django.db import models

class Contato(models.Model):
	assunto = models.CharField(verbose_name=u'Assunto', max_length=250,)
	mensagem = models.TextField(verbose_name=u'Mensagem',)
	email = models.EmailField(verbose_name=u'Email',)

	class Meta:
		verbose_name = ('contato')
		verbose_name_plural = ('contatos')

	def __unicode__(self):
		return '%s' % (self.assunto,)
    
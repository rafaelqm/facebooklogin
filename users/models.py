# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    """ User with required fields """
    facebookid = models.BigIntegerField(verbose_name='FacebookID', unique=True)
    name = models.CharField(max_length=200, verbose_name='Nome')
    username = models.CharField(max_length=200, verbose_name='Username')
    gender = models.CharField(max_length=1, verbose_name='Sexo')
    birthdate = models.DateField(verbose_name='Data de Nascimento')
    created_at = models.DateTimeField(verbose_name='Data de Cadastro', auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __unicode__(self):
        return self.username

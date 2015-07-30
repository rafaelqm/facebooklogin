# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebookid', models.BigIntegerField(verbose_name=b'FacebookID')),
                ('name', models.CharField(max_length=200, verbose_name=b'Nome')),
                ('username', models.CharField(max_length=200, verbose_name=b'Username')),
                ('gender', models.CharField(max_length=1, verbose_name=b'Sexo')),
                ('birthdate', models.DateField(verbose_name=b'Data de Nascimento')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Data de Cadastro')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
        ),
    ]

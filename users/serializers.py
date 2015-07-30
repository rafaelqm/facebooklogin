# -*- coding: utf-8 -*-
from .models import User
from rest_framework import serializers
from django.forms import widgets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('facebookid', 'name', 'username', 'gender', 'birthdate')

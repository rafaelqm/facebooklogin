# -*- coding: utf-8 -*-
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('facebookid', 'name', 'username', 'gender', 'birthdate')

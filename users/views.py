# -*- coding: utf-8 -*-
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
# from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be inserted
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

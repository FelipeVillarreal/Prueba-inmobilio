# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from Inmobilio.Prueba.models import General, Interior, Exterior
from rest_framework import viewsets
from Inmobilio.Prueba.serializers import UserSerializer, GroupSerializer, GeneralSerializer, InteriorSerializer, ExteriorSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GeneralViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = General.objects.all()
    serializer_class = GeneralSerializer

class InteriorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Interior.objects.all()
    serializer_class = InteriorSerializer

class ExteriorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Exterior.objects.all()
    serializer_class = ExteriorSerializer

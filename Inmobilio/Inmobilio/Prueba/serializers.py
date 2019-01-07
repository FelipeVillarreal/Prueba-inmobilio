from django.contrib.auth.models import User, Group
from models import General, Interior, Exterior
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class GeneralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = General
        fields = ('Tipo', 'Subtipo','Direccion','Ciudad','Departamento','Pais','Telefono')

class InteriorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interior
        fields = ('Cuartos','Banios','Closets','Calentador')

class ExteriorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exterior
        fields = ('Vigilancia','Parqueadero','Salon_social','Numero_pisos')
      

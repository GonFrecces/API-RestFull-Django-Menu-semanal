from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from ACME_APP.models import *




class PlatoSerializers(serializers.ModelSerializer):
    ingredientes = serializers.StringRelatedField(many=True)
    class Meta:
        model= Plato
        fields= ['Nombre', 'ingredientes']



class MenuSerializers(serializers.ModelSerializer):
    plato = PlatoSerializers(many=True)

    class Meta:
        model= Menu
        fields= ['Dia', 'plato']


class Plato_diasSerializers(serializers.ModelSerializer):
    class Meta:
        model= Plato
        fields= ['Dia', 'plato']


class PlatosSerializers(serializers.ModelSerializer):
    class Meta:
        model= Plato
        fields= ['Nombre']


class IngredientesSerializers(serializers.ModelSerializer):
    Plato = PlatosSerializers(read_only=True)
    class Meta:
        model= Ingredientes
        fields= ['Nombre', 'Plato']
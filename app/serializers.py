from rest_framework import serializers
from app.models import Object


class ObjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'


class ObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('name', 'lat', 'lon')

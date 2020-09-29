from django.shortcuts import render
from rest_framework import generics

from app.models import Object
from app.serializers import ObjectDetailSerializer, ObjectListSerializer


class ObjectCreateView(generics.CreateAPIView):
    serializer_class = ObjectDetailSerializer


class ObjectListView(generics.ListAPIView):
    serializer_class = ObjectListSerializer
    queryset = Object.objects.all()

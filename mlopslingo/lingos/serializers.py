from .models import Lingo, LingoType
from rest_framework import serializers


class LingoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lingo
        fields = ['name', 'description', 'lingo_type', 'created', 'updated']


class LingoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LingoType
        fields = ['name']

from .models import Lingo
from rest_framework import serializers


class LingoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lingo
        fields = ['name', 'description', 'lingo_type', 'created', 'updated']

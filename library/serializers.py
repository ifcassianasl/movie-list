from .models import Library
from rest_framework import serializers


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ['url', 'title', 'details', 'users']

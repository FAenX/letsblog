from rest_framework import serializers
from .models import User

# model serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'language')

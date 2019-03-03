from rest_framework import serializers
from django.contrib.auth.models import User

# model serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'last_login','language')

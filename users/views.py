from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UsersSerializer

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

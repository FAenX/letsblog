from django.urls import path
from .views import UserListView, signup

# andelans app url patterns

urlpatterns = [
    path('api/users/', UserListView.as_view(), name='users'),
    path('signup/', signup, name='signup'),
]

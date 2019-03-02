from django.urls import path
from .views import UserListView
# andelans app url patterns

urlpatterns = [
    path('api/users/', UserListView.as_view()),
]

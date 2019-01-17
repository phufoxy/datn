from django.urls import path
from users.views import UserRegistrationAPIView

app_name = 'users'
urlpatterns = [
    path('users/', UserRegistrationAPIView.as_view(), name="register"),
]

from django.urls import path, include
from users.views import UserEditAPIView, UserRegistrationAPIView, UserLoginAPIView, UserTokenAPIView, UserListCreateAPIView

app_name = 'users'
urlpatterns = [
    path('users/all/',include([
        path('',UserListCreateAPIView.as_view(),name='list-user'),
        path('<str:name>/',UserEditAPIView.as_view(),name='edit-user'),
    ])),
    path('users/', UserRegistrationAPIView.as_view(), name="register"),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('users/<key>/', UserTokenAPIView.as_view(), name="token"),
]

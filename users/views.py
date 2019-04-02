from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from users.serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.
# Register View Json
class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data["token"] = token.key

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

# Login View Json
class UserLoginAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

# Logout
class UserTokenAPIView(RetrieveDestroyAPIView):
    lookup_field = "key"
    serializer_class = TokenSerializer
    queryset = Token.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    def retrieve(self, request, key, *args, **kwargs):
        if key == "current":
            instance = Token.objects.get(key=request.auth.key)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return super(UserTokenAPIView, self).retrieve(request, key, *args, **kwargs)

    def destroy(self, request, key, *args, **kwargs):
        if key == "delete":
            data = [{"message":"logout success"}]
            Token.objects.get(key=request.auth.key).delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data=data)
        return super(UserTokenAPIView, self).destroy(request, key, *args, **kwargs)

# get all
class UserListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserRegistrationSerializer
    def get(self, request, format = None):
        objects = User.objects.all().order_by('-id')
        serializer = UserRegistrationSerializer(objects, many = True)
        return Response(serializer.data)



# edit user
class UserEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('name')
            print(pk)
            object = User.objects.get(username=kwargs['name'])
            serializer = UserRegistrationSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = UserRegistrationSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            User.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)
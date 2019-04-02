from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from restaurants.models import Restaurant, RestaurantDetails
from restaurants.serializers import RestaurantSerializer, RestaurantdetailSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class RestaurantListHome(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = RestaurantSerializer
    def get(self, request, format = None):
        objects = Restaurant.objects.all()
        serializer = RestaurantSerializer(objects, many = True)
        return Response(serializer.data)

class RestaurantCount(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = RestaurantSerializer
    def get(self, request, format = None):
        objects = Restaurant.objects.all()
        return Response(objects.count())

class RestaurantEditHome(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Restaurant.objects.get(pk=kwargs['pk'])
            serializer = RestaurantSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response(data={'message':'Not Page'},status=status.HTTP_404_NOT_FOUND)


# admin restaurant
class RestaurantListCreateAPIView(ListCreateAPIView):
    # The AllowAny permission class will allow unrestricted access, 
    # regardless of if the request was authenticated or unauthenticated.
    # IsAuthenticatedOrReadOnly only seem
    permission_classes = (IsAuthenticated,)
    # Call Serializer class
    serializer_class = RestaurantSerializer

    def get(self, request, format=None):
        objetcs = Restaurant.objects.all()
        serializer = RestaurantSerializer(objetcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# edit
class RestaurantEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Restaurant.objects.get(pk=kwargs['pk'])
            serializer = RestaurantSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = RestaurantSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            Restaurant.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_200_OK)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)

# admin restaurant details
class RestaurantDetailListCreateAPIView(ListCreateAPIView):
    # The AllowAny permission class will allow unrestricted access, 
    # regardless of if the request was authenticated or unauthenticated.
    # IsAuthenticatedOrReadOnly only seem
    permission_classes = (IsAuthenticated,)
    # Call Serializer class
    serializer_class = RestaurantdetailSerializer

    def get(self, request, format=None):
        objetcs = RestaurantDetails.objects.all()
        serializer = RestaurantdetailSerializer(objetcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestaurantdetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetailsEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantdetailSerializer
    queryset = RestaurantDetails.objects.all()
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = RestaurantDetails.objects.get(pk=kwargs['pk'])
            serializer = RestaurantdetailSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except RestaurantDetails.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = RestaurantdetailSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            RestaurantDetails.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_200_OK)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)
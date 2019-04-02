from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from places.models import Place, PlaceDetails
from places.serializers import PlaceSerializer, PlaceDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max, Sum, Count

# Create your views here.
# Home Places
class PlaceListHome(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PlaceSerializer
    def get(self, request, format = None):
        objects = Place.objects.all()
        serializer = PlaceSerializer(objects, many = True)
        return Response(serializer.data)

class PlaceTopHome(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PlaceSerializer
    def get(self, request, format = None):
        objects = Place.objects.all().order_by('-id')[:5]
        serializer = PlaceSerializer(objects, many = True)
        return Response(serializer.data)

class PlaceMaxHome(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PlaceSerializer
    def get(self, request, format = None):
        objects = Place.objects.all().order_by('-price')[:1]
        serializer = PlaceSerializer(objects, many = True)
        return Response(serializer.data)

class PlaceCountHome(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PlaceSerializer
    def get(self, request, format = None):
        objects = Place.objects.all()
        return Response(objects.count())


class PlaceEditHome(RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Place.objects.get(pk=kwargs['pk'])
            serializer = PlaceSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Place.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

class PlaceListCreateAPIView(ListCreateAPIView):
    # The AllowAny permission class will allow unrestricted access, 
    # regardless of if the request was authenticated or unauthenticated.
    # IsAuthenticatedOrReadOnly only seem
    permission_classes = (IsAuthenticated,)
    # Call Serializer class
    serializer_class = PlaceSerializer

    def get(self, request, format=None):
        objetcs = Place.objects.all()
        serializer = PlaceSerializer(objetcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Place.objects.get(pk=kwargs['pk'])
            serializer = PlaceSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Place.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = PlaceSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            Place.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_200_OK)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Places Details
class PlaceDetailCreateAPIView(ListCreateAPIView):
    # IsAuthenticated
    permission_classes = (IsAuthenticated,)
    serializer_class = PlaceDetailSerializer

    def get(self, request, format=None):
        objetcs = PlaceDetails.objects.all()
        serializer = PlaceDetailSerializer(objetcs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PlaceDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceDetailEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceDetailSerializer
    queryset = PlaceDetails.objects.all()
    permission_classes = (IsAuthenticated, )
    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = PlaceDetails.objects.get(pk=kwargs['pk'])
            serializer = PlaceDetailSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except PlaceDetails.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = PlaceDetailSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            PlaceDetails.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_200_OK)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from places.models import Place
from places.serializers import PlaceSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
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
                        status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)

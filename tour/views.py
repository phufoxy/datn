from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from tour.models import Tour, Image
from tour.serializers import TourSerializer, ImageSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# List Tour Home
class TourtListHome(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TourSerializer
    def get(self, request, format = None):
        objects = Tour.objects.all()
        serializer = TourSerializer(objects, many = True)
        return Response(serializer.data)

# List Id Tour
class TourEditHome(RetrieveUpdateDestroyAPIView):
    serializer_class = TourSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Tour.objects.get(pk=kwargs['pk'])
            serializer = TourSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Tour.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)
        

# admin Tour
class TourListCreateAPIView(ListCreateAPIView):
    # The AllowAny permission class will allow unrestricted access, 
    # regardless of if the request was authenticated or unauthenticated.
    # IsAuthenticatedOrReadOnly only seem
    permission_classes = (IsAuthenticated,)
    # Call Serializer class
    serializer_class = TourSerializer

    def get(self, request, format=None):
        objetcs = Tour.objects.all()
        serializer = TourSerializer(objetcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# edit
# edit
class TourEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TourSerializer
    queryset = Tour.objects.all()
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Tour.objects.get(pk=kwargs['pk'])
            serializer = TourSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Tour.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = TourSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            Tour.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)

# admin Tour
class ImageListCreateAPIView(ListCreateAPIView):
    # The AllowAny permission class will allow unrestricted access, 
    # regardless of if the request was authenticated or unauthenticated.
    # IsAuthenticatedOrReadOnly only seem
    permission_classes = (IsAuthenticated,)
    # Call Serializer class
    serializer_class = ImageSerializer

    def get(self, request, format=None):
        objetcs = Image.objects.all()
        serializer = ImageSerializer(objetcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# edit
class ImageEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Tour.objects.all()
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Image.objects.get(pk=kwargs['pk'])
            serializer = ImageSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Image.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)

   
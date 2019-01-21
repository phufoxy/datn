from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from house.models import House, HouseDetails
from house.serializers import HouseSerializer, HouseDetailSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class HouseListCreateAPIView(ListCreateAPIView):
    # The AllowAny permission class will allow unrestricted access, 
    # regardless of if the request was authenticated or unauthenticated.
    # IsAuthenticatedOrReadOnly only seem
    permission_classes = (IsAuthenticated,)
    # Call Serializer class
    serializer_class = HouseSerializer

    def get(self, request, format=None):
        objetcs = House.objects.all()
        serializer = HouseSerializer(objetcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HouseEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()
    permission_classes = (IsAuthenticated, )
    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = House.objects.get(pk=kwargs['pk'])
            serializer = HouseSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except House.DoesNotExist:
            return Response(data={'message': "Not Page"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = HouseSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            House.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)

class HouseDetailCreateAPIView(ListCreateAPIView):
    # The AllowAny permission class will allow unrestricted access, 
    # regardless of if the request was authenticated or unauthenticated.
    # IsAuthenticatedOrReadOnly only seem
    permission_classes = (IsAuthenticated,)
    # Call Serializer class
    serializer_class = HouseDetailSerializer

    def get(self, request, format=None):
        objetcs = HouseDetails.objects.all()
        serializer = HouseDetailSerializer(objetcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HouseDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HouseDetailEditAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HouseDetailSerializer
    queryset = HouseDetails.objects.all()
    permission_classes = (IsAuthenticated, )
    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = HouseDetails.objects.get(pk=kwargs['pk'])
            serializer = HouseDetailSerializer(object)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except HouseDetails.DoesNotExist:
            return Response(data={'message': "Page Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, pk, format=None):
        objects = self.get_object()
        serializer = HouseDetailSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'message': "Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        objects = self.get_object()
        if objects.id:
            HouseDetails.objects.get(id=objects.id).delete()
            return Response(data={'message': "Delete Success"},
                        status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(objects)
        return Response(status=status.HTTP_204_NO_CONTENT)
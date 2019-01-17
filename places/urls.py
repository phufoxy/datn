from django.urls import path, include
from places.views import PlaceListCreateAPIView, PlaceEditAPIView

app_name = 'place'
urlpatterns = [
    path('place/',include([
        path('', PlaceListCreateAPIView.as_view(), name="list-places"),
        path('<int:pk>/',PlaceEditAPIView.as_view(),name='place-edit')
    ]))
]

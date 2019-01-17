from django.urls import path, include
from places.views import PlaceListCreateAPIView, PlaceEditAPIView, PlaceDetailCreateAPIView, PlaceDetailEditAPIView

app_name = 'place'
urlpatterns = [
    path('admin/place/',include([
        path('', PlaceListCreateAPIView.as_view(), name="list-places"),
        path('<int:pk>/',PlaceEditAPIView.as_view(),name='place-edit'),
        path('details/',include([
            path('',PlaceDetailCreateAPIView.as_view(),name='list-places-details'),
            path('<int:pk>/',PlaceDetailEditAPIView.as_view(),name='place-detail-edit')
        ]))
    ]))
]

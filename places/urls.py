from django.urls import path, include
from places.views import PlaceListCreateAPIView, PlaceEditAPIView, PlaceDetailCreateAPIView, PlaceDetailEditAPIView, PlaceListHome, PlaceEditHome

app_name = 'place'
urlpatterns = [
    path('admin/place/',include([
        path('', PlaceListCreateAPIView.as_view(), name="list-places"),
        path('<int:pk>/',PlaceEditAPIView.as_view(),name='place-edit'),
        path('details/',include([
            path('',PlaceDetailCreateAPIView.as_view(),name='list-places-details'),
            path('<int:pk>/',PlaceDetailEditAPIView.as_view(),name='place-detail-edit')
        ]))
    ])),
    path('place/',include([
        path('', PlaceListHome.as_view(),name='list-places-home'),
        path('<int:pk>/',PlaceEditHome.as_view(),name='list-place-edit-home'),
    ]))
]

from django.urls import path, include
from house.views import HouseCount,HouseEditHome, HouseListHome, HouseListCreateAPIView, HouseEditAPIView, HouseDetailCreateAPIView, HouseDetailEditAPIView
app_name = 'house'
urlpatterns = [
    path('admin/house/',include([
        path('', HouseListCreateAPIView.as_view(), name="list-house"),
        path('<int:pk>/',HouseEditAPIView.as_view(),name='edit-house'),
        path('details/',include([
            path('',HouseDetailCreateAPIView.as_view(),name='HouseDetailCreateAPIView'),
            path('<int:pk>/',HouseDetailEditAPIView.as_view(),name='HouseDetailEditAPIView')
        ]))
    ])),
    path('house/',include([
        path('',HouseListHome.as_view(),name='list-house-home'),
        path('<int:pk>',HouseEditHome.as_view(),name='edit-house-home'),
        path('count/',HouseCount.as_view(),name="count-house"),
    ]))
]

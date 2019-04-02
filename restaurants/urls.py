from django.urls import path, include
from restaurants.views import RestaurantCount, RestaurantListHome, RestaurantListCreateAPIView ,RestaurantEditAPIView, RestaurantEditHome, RestaurantDetailListCreateAPIView, RestaurantDetailsEditAPIView

app_name = 'restaurants'
urlpatterns = [
    path('admin/restaurants/',include([
        path('',RestaurantListCreateAPIView.as_view(),name='list-restaurant'),
        path('<int:pk>/',RestaurantEditAPIView.as_view(),name='edit-restaurant'),
        path('details/',include([
            path('',RestaurantDetailListCreateAPIView.as_view(),name='list-detail-restaurant'),
            path('<int:pk>/',RestaurantDetailsEditAPIView.as_view(),name='edit-detail-restaurant'),
        ])),
        
    ])),
    path('restaurants/',include([
        path('', RestaurantListHome.as_view(),name='list-restaurant-home'),
        path('count/',RestaurantCount.as_view(),name='list-count-home'),
        path('<int:pk>/',RestaurantEditHome.as_view(),name='restaurant-edit-home'),
    ]))
]

from django.urls import path, include
from tour.views import TourtListHome, TourEditHome, TourListCreateAPIView, TourEditAPIView, ImageListCreateAPIView, ImageEditAPIView

app_name = 'tour'
urlpatterns = [
    path('admin/image/',include([
        path('', ImageListCreateAPIView.as_view(),name='list-image-admin'),
        path('<int:pk>/', ImageEditAPIView.as_view(),name='edit-image-admin'),
    ])),
    path('admin/tour/',include([
         path('', TourListCreateAPIView.as_view(),name='list-tour-admin'),
         path('<int:pk>/',TourEditAPIView.as_view(),name='edit-tour-admin'),
    ])),
    path('tour/',include([
        path('', TourtListHome.as_view(),name='list-tour-home'),
        path('<int:pk>/', TourEditHome.as_view(),name='edit-tour-home')
    ]))
]

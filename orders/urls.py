from django.urls import path
from .views import LocationListCreateAPIView, PreOrderAPIView, \
    DriverListCreateAPIView, OrderListCreateAPIVIew, \
    DriverDetailAPIView, LocationDetailAPIView 


urlpatterns = [
    path('locations', LocationListCreateAPIView.as_view()),
    path('locations/<int:pk>/', LocationDetailAPIView.as_view()),
    path('pre-orders', PreOrderAPIView.as_view()),
    path('drivers', DriverListCreateAPIView.as_view()),
    path('drivers/<int:pk>/', DriverDetailAPIView.as_view()),
    path('orders', OrderListCreateAPIVIew.as_view()),
]
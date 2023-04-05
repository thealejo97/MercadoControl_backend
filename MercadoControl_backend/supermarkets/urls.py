from django.urls import path
from .views import *

urlpatterns = [
    path('', SupermarketListAPIView.as_view(), name='list_supermarket'),
    path('<int:pk>/', SupermarketDetailAPIView.as_view(), name='detail_supermarket'),
    path('create/', SupermarketCreateAPIView.as_view(), name='create_supermarket'),
    path('update/<int:pk>/', SupermarketUpdateAPIView.as_view(), name='update_supermarket'),
    path('delete/<int:pk>/', SupermarketDeleteAPIView.as_view(), name='delete_supermarket'),
]
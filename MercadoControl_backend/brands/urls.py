from django.urls import path
from .views import *

urlpatterns = [
    path('', BrandListAPIView.as_view(), name='list_brand'),
    path('<int:pk>/', BrandDetailAPIView.as_view(), name='detail_brand'),
    path('create/', BrandCreateAPIView.as_view(), name='create_brand'),
    path('update/<int:pk>/', BrandUpdateAPIView.as_view(), name='update_brand'),
    path('delete/<int:pk>/', BrandDeleteAPIView.as_view(), name='delete_brand'),
]
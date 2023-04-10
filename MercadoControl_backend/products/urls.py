from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='list_product'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='detail_product'),
    path('create/', ProductCreateAPIView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='delete_product'),
]
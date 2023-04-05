from django.urls import path
from .views import *

urlpatterns = [
    path('', List_of_priceListAPIView.as_view(), name='list_list_of_price'),
    path('<int:pk>/', List_of_priceDetailAPIView.as_view(), name='detail_list_of_price'),
    path('create/', List_of_priceCreateAPIView.as_view(), name='create_list_of_price'),
    path('update/<int:pk>/', List_of_priceUpdateAPIView.as_view(), name='update_list_of_price'),
    path('delete/<int:pk>/', List_of_priceDeleteAPIView.as_view(), name='delete_list_of_price'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', Shopping_listListAPIView.as_view(), name='list_shopping_list'),
    path('<int:pk>/', Shopping_listDetailAPIView.as_view(), name='detail_shopping_list'),
    path('create/', Shopping_listCreateAPIView.as_view(), name='create_shopping_list'),
    path('update/<int:pk>/', Shopping_listUpdateAPIView.as_view(), name='update_shopping_list'),
    path('delete/<int:pk>/', Shopping_listDeleteAPIView.as_view(), name='delete_shopping_list'),
]
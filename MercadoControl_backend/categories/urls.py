from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='list_category'),
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name='detail_category'),
    path('create/', CategoryCreateAPIView.as_view(), name='create_category'),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='update_category'),
    path('delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='delete_category'),
]
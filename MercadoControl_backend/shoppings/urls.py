from django.urls import path
from .views import *

urlpatterns = [
    path('', ShoppingListAPIView.as_view(), name='list_shopping'),
    path('<int:pk>/', ShoppingDetailAPIView.as_view(), name='detail_shopping'),
    path('create/', ShoppingCreateAPIView.as_view(), name='create_shopping'),
    path('update/<int:pk>/', ShoppingUpdateAPIView.as_view(), name='update_shopping'),
    path('delete/<int:pk>/', ShoppingDeleteAPIView.as_view(), name='delete_shopping'),
]
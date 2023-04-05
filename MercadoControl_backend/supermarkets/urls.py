from django.urls import path
from .views import *

urlpatterns = [
    path('create/', SupermarketCreateAPIView.as_view(), name='create_supermarket'),
    path('list/', SupermarketListAPIView.as_view(), name='list_user'),
    # path('login/', UserLoginAPIView.as_view(), name='login_user'),
    # path('update/', UserUpdateAPIView.as_view(), name='update'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('', UserListAPIView.as_view(), name='list_user'),
    path('login/', UserLoginAPIView.as_view(), name='login_user'),
    # path('update/', UserUpdateAPIView.as_view(), name='update'),
]
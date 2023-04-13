from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from . import views
from .views import *

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('', UserListAPIView.as_view(), name='list_user'),
    path('login/', UserLoginAPIView.as_view(), name='login_user'),
    path('csrf_cookie/', ensure_csrf_cookie(views.csrf_cookie_view)),
    # path('update/', UserUpdateAPIView.as_view(), name='update'),
]
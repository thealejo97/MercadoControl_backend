"""MercadoControl_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from MercadoControl_Backend.users.urls import path
from django.conf.urls.static import static
from MercadoControl_Backend import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('MercadoControl_Backend.users.urls')),
    path('api/supermarkets/', include('MercadoControl_Backend.supermarkets.urls')),
    path('api/shoppings/', include('MercadoControl_Backend.shoppings.urls')),
    path('api/shopping_list/', include('MercadoControl_Backend.shopping_lists.urls')),
    path('api/products/', include('MercadoControl_Backend.products.urls')),
    path('api/list_of_prices/', include('MercadoControl_Backend.list_of_prices.urls')),
    path('api/categories/', include('MercadoControl_Backend.categories.urls')),
    path('api/brands/', include('MercadoControl_Backend.brands.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

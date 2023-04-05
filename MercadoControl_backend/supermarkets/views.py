from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupermarketSerializer
from .models import Supermarket
from django.contrib.auth import authenticate, login

class SupermarketCreateAPIView(CreateAPIView):
    model = Supermarket
    serializer_class = SupermarketSerializer

class SupermarketListAPIView(ListAPIView):
    model = Supermarket
    serializer_class = SupermarketSerializer
    queryset = Supermarket.objects.all()
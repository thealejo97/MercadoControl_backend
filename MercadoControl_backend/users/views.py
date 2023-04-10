from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate, login

class UserCreateAPIView(APIView):
    """
    API view to create a user.

    Created: Alejandro Montaño 03-04-2023

    Usage:
    Send a POST request with the fields required username,password,currency_unit and optional fields first_name,last_name,date_joined,indicative,phone,adress.

    Returns:
    A response with a HTTP response - 201 Created: User created.

    HTTP Methods:
    POST

    Request:
    {
        "username": "string",
        "password": "string"
        ... FIELDS
    }


    Response:
    {
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "date_joined": "date",
        "currency_unit": "string-list",
        "indicative": "int",
        "phone": "int",
        "adress": "string"
    }

    Errors:
    - 400 Bad request: Bad request.
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListAPIView(ListAPIView):
    """
    API view to get all users.

    Created: Alejandro Montaño 03-04-2023

    Usage:
    Send a GET request.

    Returns:
    A response with a user list JSON format.

    HTTP Methods:
    GET

    Request:
    NONE

    Response:
    [{
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "date_joined": "date",
        "currency_unit": "string",
        "indicative": "string",
        "phone": "int",
        "adress": "string"
    }]

    Errors:
    - 403 Forbidden: Authentication credentials were not provided..
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()

from rest_framework.authtoken.models import Token

class UserLoginAPIView(APIView):
    """
    API view for user login.

    Created: Alejandro Montaño 03-04-2023

    Usage:
    Send a POST request with user credentials to obtain an access token.

    Returns:
    A response with a user object and access token if the credentials are valid.
    Otherwise, an error response with a message indicating the cause of the error.

    HTTP Methods:
    POST

    Request:
    {
        "username": "string",
        "password": "string"
    }

    Response:
    {
        "user": "string",
        "token": "string"
    }

    Errors:
    - 401 UNAUTHORIZED: Invalid username or password.
    - 401 UNAUTHORIZED: This user has been deactivated.
    """
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'user': user.username, 'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'This user has been deactivated.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
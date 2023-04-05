from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .serializers import CategorySerializer
from .models import Category

class CategoryListAPIView(ListAPIView):
    """
    API view to list all Category.

    Created: Alejandro Montaño 05-04-2023

    Usage:
    Send a GET request and the api return the information.

    Returns:
    A response with a HTTP response - 200 Ok.

    HTTP Methods:
    GET

    Request:

    Response:
    {
        "id": "int",
        "name": "string",
        "phone": "int",
        "indicative": "int",
        "adress": "string",
    }

    Errors:
    - 400 Bad request: Bad request.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveAPIView):
    """
        API view to list one Category.

        Created: Alejandro Montaño 05-04-2023

        Usage:
        Send a GET request and the id of the Category and the api return the information.

        Returns:
        A response with a HTTP response - 200 Ok.

        HTTP Methods:
        GET

        Request:
        {
        "id":"int"
        }

        Response:
        {
            "id": "int",
            "name": "string",
            "phone": "int",
            "indicative": "int",
            "adress": "string",
        }

        Errors:
        - 400 Bad request: Bad request.
        - 404 Not Found: The requested resource could not be found.
        """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateAPIView(CreateAPIView):
    """
            API view to CREATE a Category.

            Created: Alejandro Montaño 05-04-2023

            Usage:
            Send a POST request and the PARAMS of the Category and the api CREATE the Category.

            Returns:
            A response with a HTTP response - 200 Ok.

            HTTP Methods:
            POST

            Request:
            {
            "name":"string",#required
            "name": "string",
            "phone": "int",
            "indicative": "int",
s            "adress": "string",
            }

            Response:
            {
                "id": "int",
                "name": "string",
                "phone": "int",
                "indicative": "int",
                "adress": "string",
            }

            Errors:
            - 400 Bad request: Bad request.
            """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(UpdateAPIView):
    """
                API view to UPDATE a Category.

                Created: Alejandro Montaño 05-04-2023

                Usage:
                Send a patch request and the ID of the Category and the api UPDATE the Category.

                Returns:
                A response with a HTTP response - 200 Ok.

                HTTP Methods:
                PATCH

                Request:
                {
                "name": "string",#OPTION|AL
                "phone": "int",#OPTIONAL|
                "indicative": "int",#OPTIONA|L
                "adress": "string",#OPTIONAL
                }

                Response:
                {
                    "id": "int",
                    "name": "string",
                    "phone": "int",
                    "indicative": "int",
                    "adress": "string",
                }

                Errors:
                - 400 Bad request: Bad request.
                - 404 Not Found: The requested resource could not be found.
                """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteAPIView(DestroyAPIView):
    """
                    API view to DELETE a Category.

                    Created: Alejandro Montaño 05-04-2023

                    Usage:
                    Send a DELETE request and the ID of the Category and the api DELETE the Category.

                    Returns:
                    A response with a HTTP response - 200 Ok.

                    HTTP Methods:
                    DELETE

                    Request:
                    {
                    "id": "INT",
                    }

                    Response:

                    Errors:
                    - 400 Bad request: Bad request.
                    - 404 Not Found: The requested resource could not be found.
                    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .serializers import SupermarketSerializer
from .models import Supermarket

class SupermarketListAPIView(ListAPIView):
    """
    API view to list all supermarkets.

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
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer

class SupermarketDetailAPIView(RetrieveAPIView):
    """
        API view to list one supermarket.

        Created: Alejandro Montaño 05-04-2023

        Usage:
        Send a GET request and the id of the supermarket and the api return the information.

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
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer

class SupermarketCreateAPIView(CreateAPIView):
    """
            API view to CREATE a supermarket.

            Created: Alejandro Montaño 05-04-2023

            Usage:
            Send a POST request and the PARAMS of the supermarket and the api CREATE the supermarket.

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
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer

class SupermarketUpdateAPIView(UpdateAPIView):
    """
                API view to UPDATE a supermarket.

                Created: Alejandro Montaño 05-04-2023

                Usage:
                Send a patch request and the ID of the supermarket and the api UPDATE the supermarket.

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
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer

class SupermarketDeleteAPIView(DestroyAPIView):
    """
                    API view to DELETE a supermarket.

                    Created: Alejandro Montaño 05-04-2023

                    Usage:
                    Send a DELETE request and the ID of the supermarket and the api DELETE the supermarket.

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
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer
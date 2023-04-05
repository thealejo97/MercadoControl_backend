from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .serializers import ProductSerializer
from .models import Product

class ProductListAPIView(ListAPIView):
    """
    API view to list all Product.

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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveAPIView):
    """
        API view to list one Product.

        Created: Alejandro Montaño 05-04-2023

        Usage:
        Send a GET request and the id of the Product and the api return the information.

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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(CreateAPIView):
    """
            API view to CREATE a Product.

            Created: Alejandro Montaño 05-04-2023

            Usage:
            Send a POST request and the PARAMS of the Product and the api CREATE the Product.

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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(UpdateAPIView):
    """
                API view to UPDATE a Product.

                Created: Alejandro Montaño 05-04-2023

                Usage:
                Send a patch request and the ID of the Product and the api UPDATE the Product.

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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteAPIView(DestroyAPIView):
    """
                    API view to DELETE a Product.

                    Created: Alejandro Montaño 05-04-2023

                    Usage:
                    Send a DELETE request and the ID of the Product and the api DELETE the Product.

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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
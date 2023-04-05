from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .serializers import BrandSerializer
from .models import Brand

class BrandListAPIView(ListAPIView):
    """
    API view to list all Brand.

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
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailAPIView(RetrieveAPIView):
    """
        API view to list one Brand.

        Created: Alejandro Montaño 05-04-2023

        Usage:
        Send a GET request and the id of the Brand and the api return the information.

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
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandCreateAPIView(CreateAPIView):
    """
            API view to CREATE a Brand.

            Created: Alejandro Montaño 05-04-2023

            Usage:
            Send a POST request and the PARAMS of the Brand and the api CREATE the Brand.

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
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandUpdateAPIView(UpdateAPIView):
    """
                API view to UPDATE a Brand.

                Created: Alejandro Montaño 05-04-2023

                Usage:
                Send a patch request and the ID of the Brand and the api UPDATE the Brand.

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
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDeleteAPIView(DestroyAPIView):
    """
                    API view to DELETE a Brand.

                    Created: Alejandro Montaño 05-04-2023

                    Usage:
                    Send a DELETE request and the ID of the Brand and the api DELETE the Brand.

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
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
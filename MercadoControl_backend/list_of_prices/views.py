from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .serializers import List_of_priceSerializer
from .models import List_of_price


class List_of_priceListAPIView(ListAPIView):
    """
    API view to list all List_of_price.

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

    serializer_class = List_of_priceSerializer

    def get_queryset(self):
        query = List_of_price.objects.all()
        if self.request.GET.get('supermarket_id'):
            id_supermarket = self.request.GET.get('supermarket_id')
            query = query.filter(supermarket=id_supermarket)
        if self.request.GET.get('product_id'):
            id_product = self.request.GET.get('product_id')
            query = query.filter(product=id_product)
        return query

class List_of_priceDetailAPIView(RetrieveAPIView):
    """
        API view to list one List_of_price.

        Created: Alejandro Montaño 05-04-2023

        Usage:
        Send a GET request and the id of the List_of_price and the api return the information.

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
    queryset = List_of_price.objects.all()
    serializer_class = List_of_priceSerializer

class List_of_priceCreateAPIView(CreateAPIView):
    """
            API view to CREATE a List_of_price.

            Created: Alejandro Montaño 05-04-2023

            Usage:
            Send a POST request and the PARAMS of the List_of_price and the api CREATE the List_of_price.

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
    queryset = List_of_price.objects.all()
    serializer_class = List_of_priceSerializer

class List_of_priceUpdateAPIView(UpdateAPIView):
    """
                API view to UPDATE a List_of_price.

                Created: Alejandro Montaño 05-04-2023

                Usage:
                Send a patch request and the ID of the List_of_price and the api UPDATE the List_of_price.

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
    queryset = List_of_price.objects.all()
    serializer_class = List_of_priceSerializer

class List_of_priceDeleteAPIView(DestroyAPIView):
    """
                    API view to DELETE a List_of_price.

                    Created: Alejandro Montaño 05-04-2023

                    Usage:
                    Send a DELETE request and the ID of the List_of_price and the api DELETE the List_of_price.

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
    queryset = List_of_price.objects.all()
    serializer_class = List_of_priceSerializer
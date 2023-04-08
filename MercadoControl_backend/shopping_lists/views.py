from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .serializers import Shopping_listSerializer
from .models import Shopping_list

class Shopping_listListAPIView(ListAPIView):
    """
    API view to list all shoppings.

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

    serializer_class = Shopping_listSerializer

    def get_queryset(self):
        query = Shopping_list.objects.all()
        print(self)
        return query

class Shopping_listDetailAPIView(RetrieveAPIView):
    """
        API view to list one shopping_list.

        Created: Alejandro Montaño 05-04-2023

        Usage:
        Send a GET request and the id of the shopping_list and the api return the information.

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
    queryset = Shopping_list.objects.all()
    serializer_class = Shopping_listSerializer

class Shopping_listCreateAPIView(CreateAPIView):
    queryset = Shopping_list.objects.all()
    serializer_class = Shopping_listSerializer


class Shopping_listUpdateAPIView(UpdateAPIView):
    """
                API view to UPDATE a shopping_list.

                Created: Alejandro Montaño 05-04-2023

                Usage:
                Send a patch request and the ID of the shopping_list and the api UPDATE the shopping_list.

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
    queryset = Shopping_list.objects.all()
    serializer_class = Shopping_listSerializer

class Shopping_listDeleteAPIView(DestroyAPIView):
    """
                    API view to DELETE a shopping_list.

                    Created: Alejandro Montaño 05-04-2023

                    Usage:
                    Send a DELETE request and the ID of the shopping_list and the api DELETE the shopping_list.

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
    queryset = Shopping_list.objects.all()
    serializer_class = Shopping_listSerializer
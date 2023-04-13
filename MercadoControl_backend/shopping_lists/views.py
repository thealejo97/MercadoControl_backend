from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .serializers import ListOfPriceSerializer, ShoppingListSerializer
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

    Errors:
    - 400 Bad request: Bad request.
    """

    serializer_class = ShoppingListSerializer

    def get_queryset(self):
        query = Shopping_list.objects.all()

        if self.request.GET.get('user_id'):
            id_user = self.request.GET.get('user_id')
            query = query.filter(user_id=id_user)
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

        Errors:
        - 400 Bad request: Bad request.
        - 404 Not Found: The requested resource could not be found.
        """
    queryset = Shopping_list.objects.all()
    serializer_class = ShoppingListSerializer

class Shopping_listCreateAPIView(CreateAPIView):
    """

        API view to list one shopping_list.

        Created: Alejandro Montaño 10-04-2023

        Usage:
        Send a POST request with the information of an shopping_list and the api will create it.

        Returns:
        A response with a HTTP response - 200 Ok.

        HTTP Methods:
        GET

        Request:
            {
                "name": "string",
                "user": int,
                "list_of_prices": [
                    {
                        "list_of_price": "int",
                        "estimated_price": "int",
                        "amount": "int",
                        "added": "bool"
                    },
                    {
                        "list_of_price": "int",
                        "estimated_price": "int",
                        "amount": "int",
                        "added": "bool"
                    }
                ]
            }

        Response:
        {
            "id": "int",
            "name": "string",
            "user": int,
            "list_of_prices": "list"
        }

        Errors:
        - 400 Bad request: Bad request.
        - 404 Not Found: The requested resource could not be found.

    """

    queryset = Shopping_list.objects.all()
    serializer_class = ShoppingListSerializer


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
    serializer_class = ShoppingListSerializer

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
    serializer_class = ShoppingListSerializer
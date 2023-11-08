import requests
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import views

from .models import Joke
from .serializers import JokeSerializer


class JokeViewSet(APIView):
    permission_classes = [AllowAny]
    serializer_class = JokeSerializer
    api_url = 'https://official-joke-api.appspot.com/random_joke'

    def post(self, request):

        # data = JokeSerializer.data
        # return Response(data)
        response = requests.get(self.api_url)
        JokeSerializer.save_response(response.json(), response_data=response.json())
        return Response(response.json(), status=response.status_code)
        # response = requests.get(self.api_url)
        # return Response(response.json())

from rest_framework import serializers
from .models import Joke


class ResponseHandling:
    def save_response(self, response_data):
        joke_id = response_data.get("id")
        joke_category = response_data.get("type")
        joke_setup = response_data.get("setup")
        joke_punchline = response_data.get("punchline")

        request_data = Joke(
            joke_id=joke_id,
            joke_category=joke_category,
            joke_setup=joke_setup,
            joke_punchline=joke_punchline,
        )
        request_data.save()


class JokeSerializer(serializers.ModelSerializer, ResponseHandling):
    class Meta:
        model = Joke
        fields = '__all__'
        # extra_kwargs = {
        #     'joke_id': {'required': True},
        #     'joke_category': {'required': True},
        #     'joke_setup': {'required': True},
        #     'joke_punchline': {'required': True},
        # }

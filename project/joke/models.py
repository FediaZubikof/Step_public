from django.db import models

from datetime import datetime


class Joke(models.Model):
    joke_id = models.IntegerField()
    joke_category = models.CharField(max_length=100, verbose_name='Категория')
    joke_start_data = models.DateTimeField(default=datetime.now(), null=True, verbose_name='Дата создания')
    joke_setup = models.CharField(max_length=200, verbose_name='Шутка')
    joke_punchline = models.CharField(max_length=100, verbose_name='Ответ')

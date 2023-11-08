from django.urls import path

from . import views

urlpatterns = [
    path('joke/', views.JokeViewSet.as_view(), name='joke')
]

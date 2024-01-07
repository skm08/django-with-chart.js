from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('details/<str:name>/', SuicideByCountry.as_view(), name='details'),
]
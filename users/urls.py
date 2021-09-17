from django.contrib import admin
from django.urls import path, include
from users.views import registro

urlpatterns = [
    path('registro/', registro, name='registro'),
]
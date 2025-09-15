from django.contrib import admin
from django.urls import path, include
from .views import text_extraction_api

urlpatterns = [
    path('extract/', text_extraction_api, name='text_extraction_api'),
]
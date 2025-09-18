from django.contrib import admin
from django.urls import path, include
from .views import text_extraction_api
from .interview_practive import start_interview, respond_to_interview

urlpatterns = [
    path('similarity/', text_extraction_api, name='text_extraction_api'),
    path('interview/start/', start_interview, name='start_interview'),
    path('interview/respond/', respond_to_interview, name='respond_to_interview'),
]
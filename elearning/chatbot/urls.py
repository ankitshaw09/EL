from django.urls import path
from .views import *

urlpatterns = [
    path("chat/", chatbot_response, name="chatbot_response"),
]

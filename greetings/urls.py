# maths/urls.py
from django.urls import path  # type: ignore
from .views import greetings, greetings_with_name

urlpatterns = [
   path('', greetings),
   path('<name>', greetings_with_name)
]

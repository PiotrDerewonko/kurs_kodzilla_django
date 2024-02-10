from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greetings(request):
   return HttpResponse("Hello World!")

def greetings_with_name(request, name):
    return HttpResponse(f"Hello {name}!")
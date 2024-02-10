from django.http import HttpResponse
from django.template import loader

def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}
    return HttpResponse(t.render(c))


def sub(request, a, b):
    a, b = int(a), int(b)
    wynik = a - b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "dodawanie"}
    return HttpResponse(t.render(c))


def mul(request, a, b):
    a, b = int(a), int(b)
    wynik = a * b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik, "title": "dodawanie"}
    return HttpResponse(t.render(c))


def div(request, a, b):
    a, b = int(a), int(b)
    wynik = a / b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dodawanie"}
    return HttpResponse(t.render(c))

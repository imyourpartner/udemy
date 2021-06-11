from django.shortcuts import render, HttpResponse

# Create your views here.


def prueba(request):
    breakpoint()
    title = "<h1>Django Website</h1>"
    body = "<h3>Building a website with Django Framework 3.2</h3>"
    for x in range(5):
        body
    return HttpResponse(title, body)

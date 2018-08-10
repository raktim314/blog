from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, you're at right place")
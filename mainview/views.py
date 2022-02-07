from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the light+fog root.")
    return render(request, 'mainview/index.html')

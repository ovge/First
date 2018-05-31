from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

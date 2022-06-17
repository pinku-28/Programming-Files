from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# /products -> index
# URL = uniform resource locator (address)


def index(request):
    return HttpResponse('Hello world')


def new(request):
    return HttpResponse('new products XD')

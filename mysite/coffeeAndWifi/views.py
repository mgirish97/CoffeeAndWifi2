from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('you are at the coffee index.')

# Create your views here.

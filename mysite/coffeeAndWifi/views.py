from django.shortcuts import render

def index(request):
    return render(request, 'coffeeAndWifi/index.html')

# Create your views here.

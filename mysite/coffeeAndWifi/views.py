from django.shortcuts import render
from coffeeAndWifi.models import Cafe

def get_three_cafes():
    cafe_list = Cafe.objects.all()[:3]
    return cafe_list


def index(request):
    context = {'cafe_list': get_three_cafes()}
    return render(request, 'coffeeAndWifi/index.html', context)

# Create your views here.

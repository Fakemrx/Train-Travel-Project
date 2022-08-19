from django.shortcuts import render
from .models import City


def show_cities(request):
    qs = City.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'cities/home.html', context=context)


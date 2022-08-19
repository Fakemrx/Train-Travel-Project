from django.shortcuts import render
from .models import City


def show_cities(request, pk=None):
    if pk:
        city = City.objects.filter(id=pk).first()
        context = {
            'city': city
        }
        return render(request, 'cities/details.html', context=context)
    qs = City.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'cities/home.html', context=context)

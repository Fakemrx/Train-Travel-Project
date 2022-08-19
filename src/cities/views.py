from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .city_add_form import CityAddForm
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


def add_city(request):
    # if request.user.is_staff or request.user.is_superuser:
    #     raise Http404
    form = CityAddForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
        'create_or_edit': 'Create',
    }
    return render(request, 'cities/city_add_form.html', context)
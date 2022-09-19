from django.shortcuts import render
from routes.route_form import RouteForm


def home(request):
    form = RouteForm
    context = {
        'form': form
    }
    return render(request, 'routes/home.html', context=context)

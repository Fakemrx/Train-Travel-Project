from django.contrib import messages
from django.shortcuts import render
from routes.route_form import RouteForm


def home(request):
    form = RouteForm
    context = {
        'form': form
    }
    return render(request, 'routes/home.html', context=context)


def find_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        context = {
            'form': form
        }
        return render(request, 'routes/home.html', context=context)
    else:
        form = RouteForm()
        messages.error(request, 'Не удалось найти путь')
        context = {
            'form': form
        }
        return render(request, 'routes/home.html', context=context)

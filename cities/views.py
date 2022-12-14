from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .city_form import CityForm
from .models import City


class CityListView(ListView):
    paginate_by = 9
    model = City
    template_name = 'cities/home.html'


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Вы добавили город'


class CityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Вы обновили город'


class CityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Вы удалили город'

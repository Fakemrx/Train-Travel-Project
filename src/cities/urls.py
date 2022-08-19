from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cities, name='home')
]
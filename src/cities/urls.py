from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cities, name='city_home'),
    path('details/<int:pk>/', views.show_cities, name='city_details'),
    path('add/', views.add_city, name='city_add'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cities, name='city_home'),
    path('<int:pk>/', views.show_cities, name='city_details'),
]
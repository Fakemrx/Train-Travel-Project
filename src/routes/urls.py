from django.urls import path, include
from routes import views

urlpatterns = [
    path('', views.home),
]

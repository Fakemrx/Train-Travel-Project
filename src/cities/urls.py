from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='home'),
    path('details/<int:pk>/', views.CityDetailView.as_view(), name='detail'),
    path('add/', views.CityCreateView.as_view(), name='add'),
    path('details/<int:pk>/edit', views.CityUpdateView.as_view(), name='update'),
    path('details/<int:pk>/delete', views.CityDeleteView.as_view(), name='delete'),
]
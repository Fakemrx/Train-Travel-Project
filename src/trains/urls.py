from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainListView.as_view(), name='home'),
    path('details/<int:pk>/', views.TrainDetailView.as_view(), name='detail'),
    path('add/', views.TrainCreateView.as_view(), name='add'),
    path('details/<int:pk>/edit', views.TrainUpdateView.as_view(), name='update'),
    path('details/<int:pk>/delete', views.TrainDeleteView.as_view(), name='delete'),
]
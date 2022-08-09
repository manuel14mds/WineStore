from django.urls import path
from . import views

urlpatterns = [
    path('varietal/', views.varietal_func, name='varietal'),
    
]
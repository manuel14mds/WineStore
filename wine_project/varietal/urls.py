from django.urls import path
from . import views
from varietal.views import varietal_func, add_varietal

urlpatterns = [
    path('varietal/', views.varietal_func, name='varietal'),
    path('addVarietal/', views.add_varietal, name='add_varietal'),
    
]
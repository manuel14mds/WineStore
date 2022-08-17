from django.urls import path
from . import views
from varietal.views import varietal_func, add_varietal, varietal_products

urlpatterns = [
    path('varietal/', varietal_func, name='varietal'),
    path('addVarietal/', add_varietal, name='add_varietal'),
    path('varietal_products/<int:vid>/', varietal_products, name='varietal_products'),
    
]
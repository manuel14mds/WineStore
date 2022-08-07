from django.urls import path
from . import views

urlpatterns = [
    path('', views.wines, name='wines'),
    path('new-wine/', views.WineCreate.as_view(), name='wine_create'),    
]
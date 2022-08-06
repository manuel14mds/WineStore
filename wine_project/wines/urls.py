from django.urls import path
from . import views

urlpatterns = [
    path('', views.wines, name='wines'),
]
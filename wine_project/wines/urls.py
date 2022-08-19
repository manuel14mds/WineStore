from django.urls import path
from . import views

urlpatterns = [
    path('', views.wines, name='wines'),
    path('new-wine/', views.WineCreate.as_view(), name='wine_create'),
    path('search/', views.search_products, name="search"),
    path('detail/<int:id>/', views.detail_wine, name="detail"),
    path('delete-wine/<int:id>/', views.delete_wine, name="delete-wine")
    

]
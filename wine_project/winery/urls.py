from django.urls import path
from winery.views import wineries, add_winery

urlpatterns = [    
    path('addWinery', add_winery, name='add a new winery'),
    path('wineries/', wineries, name='show all wineries'),
]
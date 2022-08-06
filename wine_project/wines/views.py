from django.shortcuts import render
from .models import Wine

def wines(request):
    wine_list = Wine.objects.all()
    context = {'wine_list': wine_list}
    return render(request, 'wines/wine_list.html', context=context)



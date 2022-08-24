from django.shortcuts import redirect, render
from .models import Wine
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def wines(request):
    wine_list = Wine.objects.all()
    context = {'wine_list': wine_list}
    return render(request, 'wines/wine_list.html', context=context)

class WineCreate(LoginRequiredMixin, CreateView):
    model = Wine
    fields = '__all__'
    success_url = '/'

def search_products(request):
    search = request.GET['search']
    wines = Wine.objects.filter(name__icontains=search)  #Trae los que cumplan la condicion
    context = {'wines':wines}
    return render(request, 'wines/search.html', context=context)

def detail_wine(request, id):
    wine = Wine.objects.get(id = id)
    return render(request, 'wines/detail_wine.html', context={"wine":wine})

def delete_wine(request, id):
    wine = Wine.objects.get(id = id)
    wine.delete()
    return redirect(wines)

class WineUpdate(LoginRequiredMixin, UpdateView):
    model = Wine
    fields = '__all__'
    success_url = '/'

""" def wine_update(request, pk):
    print(request.POST)
    wine = Wine.objects.get(id = pk)
    
    wine.name = request.POST['name']
    wine.winery = request.POST['winery']
    wine.varietal = request.POST['varietal']
    wine.age = request.POST['age']
    wine.price = request.POST['price']
    wine.aviable = request.POST['aviable']
    wine.image = request.POST['image']
    wine.save()
    
    return redirect(wines) """

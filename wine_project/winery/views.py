from django.shortcuts import render
from winery.models import Winery

def add_winery(request):
    if request.method == 'POST':
        Winery.objects.create(name=request.POST['name'], specialty=request.POST['specialty'], owner_name=request.POST['owner_name'])
    
    return render(request,'winery/addWinery.html', context={})


def wineries(request):
    wineries = Winery.objects.all()
    context= {
        'wineries':wineries,
        'listVoid':len(wineries)==0
    }
    return render(request, 'winery/wineries.html', context=context)

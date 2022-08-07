from django.shortcuts import render
from .models import varietal

def varietal(request):
    varietal_list = varietal.objects.all()
    context = {
        'varietal_list':varietal_list
    }
    return render(request, 'varietal/varietal_list.html', context=context)

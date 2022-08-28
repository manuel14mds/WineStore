from django.shortcuts import redirect, render
from .models import varietal
from wines.models import Wine
from varietal.forms import form_varietal


def add_varietal(request):
        
    if request.method == 'POST':
        form = form_varietal(request.POST)

        if form.is_valid():
            varietal.objects.create(
                name = form.cleaned_data['name'],
                features = form.cleaned_data['features'],
                type_grape = form.cleaned_data['type_grape'],
                location = form.cleaned_data['location'],
            )
            return redirect(varietal_func)

    elif request.method == 'GET':
        form = form_varietal()
        context = {'form' :form}
        return render(request, 'varietal/addVarietal.html', context=context)
    
def varietal_func(request):
    varietal_list = varietal.objects.all()
    context = {
        'varietal_list':varietal_list
    }
    return render(request, 'varietal/varietal_list.html', context=context)

def varietal_products(request, vid):
    var = varietal.objects.get(pk=vid)
    wine_list = Wine.objects.filter(varietal=var)

    return render(request, 'varietal/varietal_products.html', context={'varietal':var, 'wine_list':wine_list})

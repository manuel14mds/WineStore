from django.shortcuts import render

def home(request):
    return render(request,'index.html',context={})

def about_us(request):
    return render(request,'about.html',context={})
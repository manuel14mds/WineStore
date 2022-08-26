from email.headerregistry import Address
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout, authenticate
from wine_project.views import home

from users.forms import User_registration_form

from .models import User_profile


def login_request(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'Welcome {username}!!'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Not the right form', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_request)
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})

def show_profile(request, username):
    if request.method == 'POST':
        user = User_profile.objects.get(username=username)
        user.phone = request.POST['phone']
        user.address = request.POST['address']
        user.save()
        return redirect(home)

    elif request.method == 'GET':
        if request.user.is_authenticated:
            profile = request.user.profile
            context = {'profile': profile}
            return render(request, 'users/profile.html', context=context)

def create_profile(request):
    if request.method == 'POST':
        User_profile.objects.create(
            user=request.user,
            phone=request.POST['phone'],
            address=request.POST['address'],
            # image=request.POST['image']
        )
    return render(request,'users/create_profile.html', context={})
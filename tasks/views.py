from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Vehiculo

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error':'Username already exist'
                })
        return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error':'password do not match'
                })
    
def tasks(request):
    return render(request, 'tasks.html')

def signout (request):
    logout(request)
    return redirect('Home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm 
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Username o password is incorrect' 
            })
        else:
            login(request, user)
            return redirect('tasks')

def choose(request):
        if request.user.is_authenticated:
            return render(request, 'choose-section.html')
        else:
            return render(request, 'home.html')
        
def grid(request):
    if request.user.is_authenticated:
        return render(request, 'grid-store.html')
    else:
        return render(request, 'home.html')
    
def inventario(request,categoria=None):
    inventario=Vehiculo.objects.values()
    if request.method == 'POST':
        categoria = request.POST.get('my_button')
    if categoria:
        inventario = inventario.filter(categoria=categoria)
    datos = {'inventario':inventario}
    return render(request, 'inventario.html', datos)

"""def inventario(request, categoria=None):
    inventario=Vehiculo.objects.all
    print(inventario)
    if categoria:
        inventario = inventario.filter(categoria=categoria)
    datos = {'inventario':inventario}
    return render(request, 'inventario.html', datos)"""

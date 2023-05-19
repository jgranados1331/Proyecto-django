from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Vehiculo,Profile,Order,OrderDetail
from .forms import Profile_form
import json
import random

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
            return redirect('Home')  
    
def inventario(request,categoria=None):
    inventario=Vehiculo.objects.values()
    if request.method == 'POST':
        categoria = request.POST.get('my_button')
    if categoria:
        inventario = inventario.filter(categoria=categoria)
    datos = {'inventario':inventario}
    return render(request, 'inventario.html', datos)

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_user = request.user
            print(current_user)
            profile = Profile.objects.create(Imagen="users-profile/"+request.POST['Imagen'],nombre=request.POST['nombre'],apellido=request.POST['apellido'],fecha_nacimiento=request.POST['fecha_nacimiento'],edad=request.POST['edad'],celular=request.POST['celular'],cc_passport=request.POST['cc_passport'],pais=request.POST['pais'],ciudad=request.POST['ciudad'],domicilio=request.POST['domicilio'],user=current_user)
            profile.save()
            return redirect('profile')
        else:
            profiles=Profile.objects.values()
            id_profile=request.user.id
            profiles_p=profiles.filter(user_id=id_profile)
            datos = {'profiles': profiles_p}
            if profiles_p.exists():
                return render(request,'Profile.html',datos)
            else:
                formulario={
                'form': Profile_form}
                return render(request,'Profile.html',formulario)
    else:
        return redirect('Home')  
    
def detalle(request,slug):
        if request.user.is_authenticated:
            if Vehiculo.objects.filter(slug=slug).exists():
                vehiculo=Vehiculo.objects.get(slug=slug)
                context = {"Vehiculo":vehiculo}
                return render(request, 'detalle.html', context)
        else:
           return redirect('Home')   

def cart(request,slug):
    if request.user.is_authenticated:
            vehiculo=Vehiculo.objects.get(slug=slug)
            initial= {"items":[], "price":0.0, "count":0}
            session=request.session.get("data",initial)
            if slug in session["items"]:
                return(request,{'error':'Producto ya existe en el carrito'})
            else:
                session["items"].append(slug)
                session["price"]+= float(vehiculo.precio)
                session["count"]+= 1
                request.session["data"]=session

            return redirect("detalle",slug)
    else:
        return redirect('Home')  
    
def mycart(request):
    request.session["paypal"]=False
    sess=request.session.get("data",{"items":[]})
    print(sess)
    products=Vehiculo.objects.filter(slug__in=sess["items"])
    total = sess["price"]
    print(products)
    context= {"vehiculos":products,"total":total}
    return render(request,'mycart.html',context)
def simple_checkout(request):
    template_name='simple_checkout.html'
    return render(request,template_name)

def paymentComplete(request):
    body=json.loads(request.body)
    sess=request.session.get("data",{"items":[]})
    productoscart=sess["items"]
    Oc=Order()
    Oc.customer=body['customer']
    Oc.ordernum=random.randint(1000,99999)
    Oc.save()
    for item in productoscart:
        prod=Vehiculo.objects.get(slug=item)
        Od=OrderDetail()
        Od.product=prod
        Od.cant=1
        Od.order=Oc
        Od.save()
    del request.session['data']
    return redirect('sucess')

def sucess(request):
    template_name='sucess.html'
    return render(request,template_name)

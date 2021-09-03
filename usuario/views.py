from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # mail = form.cleaned_data['email'] <--- muchos usuarios no tienen email
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "usuario/login.html", {'form': form})


from django.contrib.auth.forms import UserCreationForm


def registro(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "usuario/registro.html", {'form': form})

from django.contrib.auth import logout as do_logout


def logout(request):
    do_logout(request)
    return redirect('/')


def home(request):
    return render(request, 'usuario/home.html')


from django.core import serializers


def results(request):
    '''
    muestra una tabla con los resultados de la partida: en proceso
    '''
    results = serializers.serialize("python", Partida.objects.all())
    ultima_partida = results[-1]
    return render(request, "usuario/results.html", {'resul': ultima_partida})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import AnuncioForm
from .models import Anuncio

# Create your views here.


def index(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'index.html',{
        'anuncios' : anuncios
    })

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('anuncio')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

@login_required(login_url='iniciar_sesion')
def anuncio(request):
    
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncio.html',{
        'anuncios' : anuncios
    })

@login_required(login_url='iniciar_sesion')
def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Username or pasword is incorrect'
            })
        else:
            login(request, user)
            return redirect('anuncio')

@login_required(login_url='iniciar_sesion')
def crear_anuncio(request):

    if request.method == 'GET':
        return render(request, 'create_anuncio.html', {
            'form': AnuncioForm
        })
    else:
        try:
            form = AnuncioForm(request.POST, request.FILES)
            new_anuncio = form.save(commit=False)
            new_anuncio.user = request.user
            new_anuncio.save()
            return redirect('anuncio')
        except ValueError:
           return render(request, 'create_anuncio.html', {
            'form': AnuncioForm,
            'error' : 'Error al guardar anuncio, revisar data'
        })
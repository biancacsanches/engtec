from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from core.models import Projeto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse



# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')


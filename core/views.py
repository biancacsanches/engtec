from django.shortcuts import render
from django.shortcuts import render, redirect
from core.models import Projeto, Cliente 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse



# Create your views here.
def dashboard(request):
    return  render(request, 'dashboard.html')
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
    return redirect('/dashboard')

def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def submit_projeto(request):
        # pylint: disable=no-member

    if request.POST:
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        status_andamento = request.POST.get('status_andamento')
        orcamento = request.POST.get('orcamento')
        data_inicio = request.POST.get('data_inicio')
        cliente = request.POST.get('cliente')
        id_projeto = request.POST.get('id_projeto')
        if (nome is not None and descricao is not None and status_andamento is not None and orcamento is not None and data_inicio is not None and cliente is not None):
            if id_projeto:
                Projeto.objects.filter(id=id_projeto).update(nome=nome, descricao=descricao, status_andamento=status_andamento, data_inicio=data_inicio, cliente = cliente)
                status = 1
            else:
                Projeto.objects.create(nome=nome, descricao=descricao, status_andamento=status_andamento, data_inicio=data_inicio, cliente = cliente)
                status = 2
        else :
            status = 3      
    return render(request, 'projeto.html', status)

@login_required(login_url='/')
def submit_cliente(request):
        # pylint: disable=no-member

    if request.POST:
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        perfil = request.POST.get('perfil')
        id_cliente = request.POST.get('id_cliente')
        if (nome is not None and  telefone is not None and email is not None and perfil is not None):
            if id_cliente:
                Cliente.objects.filter(id=id_cliente).update(nome=nome, telefone=telefone, email=email, perfil=perfil)
                status = 1
            else:
                Cliente.objects.create(nome=nome, telefone=telefone, email=email, perfil=perfil)
                status = 2
        else :
            status = 3      
    return render(request, 'projeto.html', status)

def cadastrar_cliente(request):
    return render(request, 'cadastro.html')

def lista_clientes(request):
    # pylint: disable=no-member
    cliente = Cliente.objects.all()
    dados = {'clientes':cliente}
    return render(request, 'projeto.html', dados)
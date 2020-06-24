from django.shortcuts import render
from django.shortcuts import render, redirect
from core.models import Projeto, Cliente 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse



# Create your views here.
@login_required(login_url='/')
def dashboard(request):
    cliente = Cliente.objects.all()
    projetos = Projeto.objects.all()
    dados = {'clientes':cliente , 'projetos': projetos}
    return  render(request, 'dashboard.html',dados)

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/')
def cadastro_cliente(request):
    return render(request, 'components/dashboard/pages/customerRegistration.html')

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/dashboard')
        else:
            messages.error(request, "Usuário ou senha inválido")
            return redirect('/')
            
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def submit_projeto(request):
    if request.POST:
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        status_andamento = request.POST.get('status_andamento')
        orcamento = request.POST.get('orcamento')
        data_inicio = request.POST.get('data_inicio')
        cliente = Cliente.objects.get(id=request.POST.get('cliente'))

        id_projeto = request.POST.get('id_projeto')
        if (nome is not None and descricao is not None and status_andamento is not None and orcamento is not None and data_inicio is not None and cliente is not None):
            if id_projeto:
                Projeto.objects.filter(id=id_projeto).update(nome=nome, descricao=descricao, status_andamento=status_andamento, orcamento=orcamento, data_inicio=data_inicio, cliente = cliente)
                status = {'success':1}

            else:
                Projeto.objects.create(nome=nome, descricao=descricao, status_andamento=status_andamento, orcamento=orcamento, data_inicio=data_inicio, cliente = cliente)
                status = {'success':2}

        else :
                status = {'success':3}
     
<<<<<<< HEAD
    return redirect('/dashboard')


=======
    return redirect('dashboard/projeto/cadastro')
>>>>>>> b01395a7a909dc9c293afccd26589bfc48b1e939

@login_required(login_url='/')
def submit_cliente(request):
    if request.POST:
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        perfil = request.POST.get('perfil')
        id_cliente = request.POST.get('id_cliente')

        if (nome is not None and  telefone is not None and email is not None and perfil is not None):
            if id_cliente:
                Cliente.objects.filter(id=id_cliente).update(nome=nome, telefone=telefone, email=email, perfil=perfil)
                status = {'success':1}
            else:
                Cliente.objects.create(nome=nome, telefone=telefone, email=email, perfil=perfil)
                
                status = {'success':2}
        else :
           status = {'success':3}      
<<<<<<< HEAD
    return redirect('/dashboard')
=======
    return render(request, 'cliente-cadastro.html', status)
>>>>>>> b01395a7a909dc9c293afccd26589bfc48b1e939

def lista_clientes(request):
    # pylint: disable=no-member
    cliente = Cliente.objects.all()
    dados = {'clientes':cliente}
<<<<<<< HEAD
    return render(request, 'components/dashboard/pages/projeto-cadastro.html', dados)
=======
    return render(request, 'projeto-cadastro.html', dados)
>>>>>>> b01395a7a909dc9c293afccd26589bfc48b1e939

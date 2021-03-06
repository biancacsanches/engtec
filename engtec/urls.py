"""engtec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),
    path('dashboard/', views.dashboard),
    path('dashboard/projeto/submit', views.submit_projeto),
    path('dashboard/cliente/submit', views.submit_cliente),
    path('dashboard/projeto/cadastro', views.lista_clientes),
    path('dashboard/cliente/cadastro', views.cadastro_cliente)
]
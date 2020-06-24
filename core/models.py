from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    perfil = models.CharField(max_length=100)



class Projeto (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name='Descrição')
    status_andamento = models.CharField(max_length=100, verbose_name='Status Andamento')
    orcamento = models.IntegerField(verbose_name='Orçamento')
    data_inicio = models.DateTimeField(auto_now=True, verbose_name='Data de Inicio')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def get_data_input_projeto(self):
        # pylint: disable=no-member
        return self.data_inicio.strftime('%Y-%m-%dT%H:%M')
    def get_data_projeto(self):
        # pylint: disable=no-member
        return self.data_inicio.strftime('%d/%m/%Y %H:%M hrs')


class Imagem (models.Model):
    imagem = models.BinaryField()
    descricao = models.TextField(verbose_name='Descrição')
    obra = models.ForeignKey(Projeto, on_delete=models.CASCADE)


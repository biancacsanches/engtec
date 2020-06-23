from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.
class Projeto (models.Model):
    cliente = models.CharField(max_length=100)
    descricao = models.TextField()
    orcamento = models.IntegerField(verbose_name='Orçamento')
    data_cadastro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente

    def get_data_cadastro(self):
        # pylint: disable=no-member
        return self.data_cadastro.strftime('%d/%m/%Y %H:%M hrs')
    
    def get_data_input_cadastro(self):
        # pylint: disable=no-member
        return self.data_cadastro.strftime('%Y-%m-%dT%H:%M')
    
    #def get_evento_atrasado(self):
        #if self.data_evento < datetime.now():
           # return True
        #else:
            #return False
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import datetime 

# Create your models here.

class Demanda(models.Model):
    codigo = models.CharField(max_length=100)
    def __unicode__(self):
        return '%s' % (self.codigo)


class Peca(models.Model):
    demanda = models.ManyToManyField(Demanda, related_name='pecas',null=True,)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Endereco(models.Model):
    demanda = models.ManyToManyField(Demanda, related_name='enderecos',null=True,)
    rua = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    numero = models.IntegerField()

    def __str__(self):
        return self.rua


class Contato(models.Model):
    demanda = models.ManyToManyField(Demanda, related_name='contatos',null=True,)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)

    def __str__(self):
        retorno =str(self.email) 
        return retorno



class Anunciante(models.Model):
    demanda = models.ManyToManyField(Demanda, related_name='anunciantes',null=True,)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

'''
class Status(models.Model):
    demanda = models.ForeignKey(Demanda, related_name='status', on_delete=models.CASCADE)
    upload = models.FileField(upload_to='uploads/')
'''

   

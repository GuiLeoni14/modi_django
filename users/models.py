from django.db import models
from django.contrib import admin
# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

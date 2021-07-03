from django.db import models


# Create your models here.
class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    senha = models.CharField(max_length=8)


class Contato(models.Model):
    idcontato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    fone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    idusuario = models.ForeignKey(Usuario, null=False, on_delete=models.RESTRICT)


class Compromisso(models.Model):
    idcompromisso = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=300)
    local = models.CharField(max_length=100)
    data = models.DateField()
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.RESTRICT)
    idcontato = models.ForeignKey(Contato, null=False, on_delete=models.RESTRICT)

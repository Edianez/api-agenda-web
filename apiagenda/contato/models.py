from django.db import models
from apiagenda.usuario import models as usuModels


# Create your models here.
class Contato(models.Model):
    idcontato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    fone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    idusuario = models.ForeignKey(usuModels.Usuario, null=False, on_delete=models.RESTRICT)

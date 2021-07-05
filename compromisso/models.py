from django.db import models
from usuario import models as usuModels
from contato import models as conModels


# Create your models here.
class Compromisso(models.Model):
    idcompromisso = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=300)
    local = models.CharField(max_length=100)
    data = models.DateField()
    usuario = models.ForeignKey(usuModels.Usuario, null=False, on_delete=models.RESTRICT)
    idcontato = models.ForeignKey(conModels.Contato, null=False, on_delete=models.RESTRICT)

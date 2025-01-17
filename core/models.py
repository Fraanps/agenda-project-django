from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data de criação") # isere a hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # quando o usuario for excluido, exclui os eventos dele


    class Meta:
        db_table = 'evento'


    def __str__(self):
        return self.titulo     # para retornar o nome do titulo do evento
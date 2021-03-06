from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Categoria(models.Model):
   tipo_categoria = models.CharField(max_length=150)

   def __str__(self):
      return self.tipo_categoria

class Receita(models.Model):
   nome_receita = models.CharField(max_length=200, verbose_name='nome da receita')
   ingredientes = models.TextField()
   modo_preparo = models.TextField()
   tempo_preparo = models.IntegerField(verbose_name='tempo de preparo')
   rendimento = models.CharField(max_length=50)
   data_publicacao = models.DateTimeField(default=datetime.now, blank=True)
   data_modificacao = models.DateTimeField(auto_now=True)
   publicada = models.BooleanField(default=False)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receitas', verbose_name='criado por')
   categoria = models.ManyToManyField(Categoria, related_name='receitas', default='Sem categoria')
   foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

   def __str__(self):
      return self.nome_receita
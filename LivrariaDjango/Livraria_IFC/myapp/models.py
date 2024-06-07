from django.db import models
from django.core.validators import MinLengthValidator
# Database models
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.IntegerField()

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], validators=[MinLengthValidator(1)])

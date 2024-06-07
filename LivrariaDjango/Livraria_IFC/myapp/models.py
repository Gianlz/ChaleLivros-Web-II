from django.db import models
from django.core.validators import MinLengthValidator

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()

    def __str__(self):
        return self.nome  # Display book name in admin panel

class Usuario(models.Model):
    MASCULINO = 'M'
    FEMININO = 'F'
    GENERO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)  # Consider using password hashing for security
    telefone = models.CharField(max_length=15)
    nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)

    def __str__(self):
        return self.nome  # Display user name in admin panel

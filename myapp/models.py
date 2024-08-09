# models.py

from django.db import models
import logging

# Obtém um logger para o modelo Livro
livro_logger = logging.getLogger('livro_logger')

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        livro_logger.debug(f'Livro salvo: {self.nome}')
        super().save(*args, **kwargs)


# Obtém um logger para o modelo Usuario
usuario_logger = logging.getLogger('usuario_logger')

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
        return self.nome

    def save(self, *args, **kwargs):
        usuario_logger.debug(f'Usuário salvo: {self.nome}')
        super().save(*args, **kwargs)


# Obtém um logger para o modelo GoogleUser
googleuser_logger = logging.getLogger('googleuser_logger')

class GoogleUser(models.Model):
    google_id = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    imagem_url = models.URLField()

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        googleuser_logger.debug(f'Usuário do Google salvo: {self.nome}')
        super().save(*args, **kwargs)

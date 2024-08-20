# models.py

from django.db import models
from djongo import models
import logging

# Obtém um logger para o modelo Livro
livro_logger = logging.getLogger('livro_logger')

class Livro(models.Model):

    categoria_choices = [
        ('Ação', 'Ação'),
        ('Aventura', 'Aventura'),
        ('Ficção Científica', 'Ficção Científica'),
        ('Romance', 'Romance'),
        ('Tecnologia', 'Tecnologia'),
        ('Terror', 'Terror'),
    ]

    _id = models.ObjectIdField()
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=categoria_choices, default='Ação')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    paginas = models.PositiveIntegerField()
    sinopse = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    capa = models.FileField(upload_to='capa')

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        livro_logger.debug(f'Livro salvo: {self.nome}')
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

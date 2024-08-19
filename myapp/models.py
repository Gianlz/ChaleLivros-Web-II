
from django.db import models
import logging
import uuid

livro_logger = logging.getLogger('livro_logger')

class Livro(models.Model):

    categoria_choices = (
        ('Ação', 'Ação'),
        ('Aventura', 'Aventura'),
        ('Ficção Científica', 'Ficção Científica'),
        ('Romance', 'Romance'),
        ('Tecnologia', 'Tecnologia'),
        ('Terror', 'Terror'),
    )
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=4, choices=categoria_choices, default='AC')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    paginas = models.PositiveIntegerField()
    sinopse = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    capa = models.FileField(upload_to='capa')

    def str(self):
        return self.nome

    def save(self, args, **kwargs):
        livro_logger.debug(f'Livro salvo: {self.nome}')
        super().save(args, kwargs)


googleuser_logger = logging.getLogger('googleuser_logger')

class GoogleUser(models.Model):
    google_id = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    imagem_url = models.URLField()

    def str(self):
        return self.nome

    def save(self, *args, kwargs):
        googleuser_logger.debug(f'Usuário do Google salvo: {self.nome}')
        super().save(*args, **kwargs)
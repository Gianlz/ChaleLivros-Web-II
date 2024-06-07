from django.contrib import admin

# Register your models here.


from .models import Livro, Usuario

admin.site.register(Livro)
admin.site.register(Usuario)

from django.contrib import admin
from .models import Usuario


# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "sobrenome", "email", "whatsapp", "data_nascimento")
    list_display_links = ("id", "nome", "sobrenome", "email", "whatsapp", "data_nascimento")
    list_per_page = 30

admin.site.register(Usuario, UsuarioAdmin)
# Register your models here.

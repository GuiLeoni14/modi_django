from users.models import Usuario
from django.forms import ModelForm


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','sobrenome', 'email', 'whatsapp', 'data_nascimento']
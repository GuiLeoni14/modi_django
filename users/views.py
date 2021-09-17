from django.shortcuts import render, redirect
from users.models import Usuario
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def registro(request):
    if request.POST:
        nome = request.POST["nome"]
        sobrenome = request.POST["sobrenome"]
        email = request.POST["email"]
        whatsapp = request.POST["whatsapp"]
        data_nascimento = request.POST["data_nascimento"]
        registro_usuario = Usuario.objects.create(
            nome=nome, sobrenome=sobrenome, email=email, whatsapp=whatsapp, data_nascimento=data_nascimento
            )
        registro_usuario.save()
        return redirect("home")
    return render(request, 'template/registro.html')

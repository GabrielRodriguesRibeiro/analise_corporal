from django.shortcuts import render, redirect
from django.contrib import messages  # precisa importar isso
from cadastro_usuario.models import Usuario

# Create your views here
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = Usuario.objects.filter(email=email, senha=senha).first()

        if usuario:
            return redirect('formulario_corpo.html')
        else:
            messages.error(request, 'Email ou senha inválidos')
            return redirect('login.html')
    else:
        return render(request, 'login.html')

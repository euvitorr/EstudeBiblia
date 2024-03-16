from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_without_params')
        else:
            messages.error(request, "Seu nome de usuário ou senha estão incorretos")
            return redirect('login')
    return render(request, 'login.html')

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

@login_required
def atualizar_perfil_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'atualizar_perfil.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redireciona para a página inicial do app biblia
    # Altere '/' para o nome da sua URL de home se necessário, por exemplo, redirect('nome_da_url_home')
    return redirect('/')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from .models import Perfil
from .forms import PerfilForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re
from django.shortcuts import get_object_or_404
from cartas.models import Carta


def cadastro(request):

    if request.method == 'POST':

        nome = request.POST.get(
            'nome'
        )

        username = request.POST.get(
            'username'
        )

        email = request.POST.get(
            'email'
        )

        senha = request.POST.get(
            'senha'
        )

        # USERNAME JÁ EXISTE
        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Esse usuário já está em uso.'
            )

            return redirect('cadastro')

        # SENHA MÍNIMA
        if len(senha) < 8:

            messages.error(
                request,
                'A senha deve ter pelo menos 8 caracteres.'
            )

            return redirect('cadastro')

        # SENHA MÁXIMA
        if len(senha) > 30:

            messages.error(
                request,
                'A senha pode ter no máximo 30 caracteres.'
            )

            return redirect('cadastro')

        # LETRA MAIÚSCULA
        if not re.search(
            r'[A-Z]',
            senha
        ):

            messages.error(
                request,
                'A senha precisa ter uma letra maiúscula.'
            )

            return redirect('cadastro')

        # NÚMERO
        if not re.search(
            r'[0-9]',
            senha
        ):

            messages.error(
                request,
                'A senha precisa ter um número.'
            )

            return redirect('cadastro')

        # CRIA USUÁRIO
        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        # CRIA PERFIL
        Perfil.objects.create(
            user=usuario,
            nome=nome
        )

        login(request, usuario)

        return redirect('home')

    return render(
        request,
        'cadastro.html'
    )


def login_usuario(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username=username,
            password=senha
        )

        if usuario:
            login(request, usuario)
            return redirect('home')
    return render(request, 'login.html')


def logout_usuario(request):
    logout(request)
    return redirect('home')

@login_required
def perfil(request):

    perfil, criado = Perfil.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        'perfil.html',
        {
            'perfil': perfil
        }
    )


@login_required
def editar_perfil(request):

    perfil, criado = Perfil.objects.get_or_create(
        user=request.user
    )

    form = PerfilForm(
        request.POST or None,
        request.FILES or None,
        instance=perfil
    )

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            return redirect('perfil')

    return render(
        request,
        'editar_perfil.html',
        {
            'form': form
        }
    )

def perfil_publico(request, username):

    usuario = get_object_or_404(
        User,
        username=username
    )

    perfil = usuario.perfil

    cartas = Carta.objects.filter(
        autor=usuario
    ).order_by('-criado_em')

    return render(
        request,
        'perfil_publico.html',
        {
            'usuario_perfil': usuario,
            'perfil': perfil,
            'cartas': cartas,
        }
    )
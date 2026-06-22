from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from datetime import timedelta

from django.utils import timezone

from unidecode import unidecode

from .forms import (
    CartaForm,
    ComentarioForm
)

from .models import (
    Carta,
    Curtida,
    Comentario,
    Adocao,
    Notificacao
)


@login_required
def criar_carta(request):

    form = CartaForm(
        request.POST or None,
        request.FILES or None
    )

    ultima_carta = Carta.objects.filter(
        autor=request.user
    ).order_by('-criado_em').first()

    if ultima_carta:

        limite = ultima_carta.criado_em + timedelta(days=7)

        if timezone.now() < limite:

            return render(
                request,
                'criar_carta.html',
                {
                    'form': form,
                    'erro_limite': True
                }
            )

    if form.is_valid():

        carta = form.save(commit=False)

        carta.autor = request.user

        perfil = request.user.perfil

        carta.cidade = perfil.cidade
        carta.estado = perfil.estado
        
        carta.save()

        return redirect('feed')

    return render(
        request,
        'criar_carta.html',
        {
            'form': form
        }
    )


def feed(request):

    cartas = Carta.objects.all().order_by(
        '-criado_em'
    )

    pesquisa = request.GET.get('pesquisa')

    cidade = request.GET.get('cidade')

    estado = request.GET.get('estado')

    adotado = request.GET.get('adotado')

    # PESQUISA
    if pesquisa:

        pesquisa_normalizada = unidecode(
            pesquisa.lower()
        )

        cartas_filtradas = []

        for carta in cartas:

            titulo = unidecode(
                carta.titulo.lower()
            )

            texto = unidecode(
                carta.texto.lower()
            )

            if (
                pesquisa_normalizada in titulo
                or
                pesquisa_normalizada in texto
            ):

                cartas_filtradas.append(
                    carta
                )

        cartas = cartas_filtradas

    # CIDADE
    if cidade:

        cartas = [
            carta for carta in cartas
            if cidade.lower()
            in carta.cidade.lower()
        ]

    # ESTADO
    if estado:

        cartas = [
            carta for carta in cartas
            if estado.lower()
            in carta.estado.lower()
        ]

    # ADOÇÃO
    if adotado == 'sim':

        cartas = [
            carta for carta in cartas
            if carta.adotado
        ]

    elif adotado == 'nao':

        cartas = [
            carta for carta in cartas
            if not carta.adotado
        ]

    for carta in cartas:

        carta.usuario_curtiu = carta.curtidas.filter(
            usuario=request.user
        ).exists() if request.user.is_authenticated else False

    return render(
        request,
        'feed.html',
        {
            'cartas': cartas
        }
    )


@login_required
def curtir_carta(request, carta_id):

    carta = get_object_or_404(
        Carta,
        id=carta_id
    )

    curtida = carta.curtidas.filter(
        usuario=request.user
    )

    # DESCURTIR
    if curtida.exists():

        curtida.delete()

    # CURTIR
    else:

        Curtida.objects.create(
            usuario=request.user,
            carta=carta
        )

    return redirect(
        'detalhe_carta',
        id=carta.id
    )


@login_required
def comentar_carta(request, carta_id):

    carta = get_object_or_404(
        Carta,
        id=carta_id
    )

    form = ComentarioForm(
        request.POST or None
    )

    if form.is_valid():

        comentario = form.save(commit=False)

        comentario.usuario = request.user

        comentario.carta = carta

        comentario.save()

    return redirect(
        'detalhe_carta',
        id=carta.id
    )


@login_required
def adotar_carta(request, carta_id):

    carta = get_object_or_404(
        Carta,
        id=carta_id
    )

    # NÃO PODE ADOTAR A PRÓPRIA CARTA
    if carta.autor == request.user:

        return redirect(
            'detalhe_carta',
            id=carta.id
        )

    adocao = Adocao.objects.filter(
        carta=carta
    ).first()

    # JÁ ADOTADA
    if adocao:

        # DESFAZER ADOÇÃO
        if adocao.usuario == request.user:

            adocao.delete()

            carta.adotado = False

            carta.save()

        return redirect(
            'detalhe_carta',
            id=carta.id
        )

    # CRIAR ADOÇÃO
    Adocao.objects.create(
        usuario=request.user,
        carta=carta
    )

    carta.adotado = True

    carta.save()

    # NOTIFICAÇÃO
    Notificacao.objects.create(
        usuario=carta.autor,
        mensagem=f'{request.user.username} adotou seu desejo!'
    )

    return redirect(
        'detalhe_carta',
        id=carta.id
    )


@login_required
def notificacoes(request):

    notificacoes = Notificacao.objects.filter(
        usuario=request.user
    ).order_by('-criado_em')

    notificacoes.update(
        lida=True
    )

    return render(
        request,
        'notificacoes.html',
        {
            'notificacoes': notificacoes
        }
    )


def detalhe_carta(request, id):

    carta = get_object_or_404(
        Carta,
        id=id
    )

    carta.usuario_curtiu = False

    if request.user.is_authenticated:

        carta.usuario_curtiu = carta.curtidas.filter(
            usuario=request.user
        ).exists()

    return render(
        request,
        'detalhe_carta.html',
        {
            'carta': carta
        }
    )


@login_required
def apagar_carta(request, id):

    carta = get_object_or_404(
        Carta,
        id=id,
        autor=request.user
    )

    carta.delete()

    return redirect('perfil')


@login_required
def correspondido_carta(request, id):

    carta = get_object_or_404(
        Carta,
        id=id,
        autor=request.user
    )

    carta.correspondido = True

    carta.save()

    return redirect('perfil')
from django.shortcuts import render

from cartas.models import Carta

from unidecode import unidecode


def home(request):

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

    return render(
        request,
        'home.html',
        {
            'cartas': cartas
        }
    )

def faq(request):

    return render(
        request,
        'faq.html'
    )
from django.urls import path
from . import views

urlpatterns = [

    path(
        'criar/',
        views.criar_carta,
        name='criar_carta'
    ),

    path(
        '',
        views.feed,
        name='feed'
    ),

    path(
        'curtir/<int:carta_id>/',
        views.curtir_carta,
        name='curtir_carta'
    ),

    path(
        'comentar/<int:carta_id>/',
        views.comentar_carta,
        name='comentar_carta'
    ),

    path(
        'adotar/<int:carta_id>/',
        views.adotar_carta,
        name='adotar_carta'
    ),

    path(
        'notificacoes/',
        views.notificacoes,
        name='notificacoes'
    ),

    path(
        '<int:carta_id>/',
        views.detalhe_carta,
        name='detalhe_carta'
),

    path(
        'carta/<int:id>/',
        views.detalhe_carta,
        name='detalhe_carta'
    ),

    path(
    'apagar-carta/<int:id>/',
    views.apagar_carta,
    name='apagar_carta'
),

    path(
        'correspondido/<int:id>/',
        views.correspondido_carta,
        name='correspondido_carta'
    ),
]
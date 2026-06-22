from django import forms

from .models import (
    Carta,
    Comentario
)


class CartaForm(forms.ModelForm):

    class Meta:

        model = Carta

        fields = [
            'titulo',
            'texto',
            'imagem'
        ]


class ComentarioForm(forms.ModelForm):

    class Meta:

        model = Comentario

        fields = [
            'texto'
        ]
from django import forms

from .models import Perfil


class PerfilForm(forms.ModelForm):

    class Meta:

        model = Perfil

        fields = [
            'nome',
            'bio',
            'foto',
            'cep',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'complemento'
        ]

        widgets = {

            'cep': forms.TextInput(
                attrs={
                    'id': 'cep'
                }
            ),

            'rua': forms.TextInput(
                attrs={
                    'id': 'rua'
                }
            ),

            'bairro': forms.TextInput(
                attrs={
                    'id': 'bairro'
                }
            ),

            'cidade': forms.TextInput(
                attrs={
                    'id': 'cidade'
                }
            ),

            'estado': forms.TextInput(
                attrs={
                    'id': 'estado'
                }
            ),
        }
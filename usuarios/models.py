from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    nome = models.CharField(
        max_length=150,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    foto = models.ImageField(
        upload_to='perfis/',
        blank=True,
        null=True
    )

    cep = models.CharField(
        max_length=9,
        blank=True
    )

    rua = models.CharField(
        max_length=255,
        blank=True
    )

    numero = models.CharField(
        max_length=20,
        blank=True
    )

    bairro = models.CharField(
        max_length=100,
        blank=True
    )

    cidade = models.CharField(
        max_length=100,
        blank=True
    )

    estado = models.CharField(
        max_length=100,
        blank=True
    )

    complemento = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):

        return self.user.username
    
cep = models.CharField(
    max_length=9,
    blank=True
)

rua = models.CharField(
    max_length=255,
    blank=True
)

numero = models.CharField(
    max_length=20,
    blank=True
)

bairro = models.CharField(
    max_length=100,
    blank=True
)

cidade = models.CharField(
    max_length=100,
    blank=True
)

estado = models.CharField(
    max_length=100,
    blank=True
)

complemento = models.CharField(
    max_length=255,
    blank=True
)
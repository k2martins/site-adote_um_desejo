from django.db import models
from django.contrib.auth.models import User


class Carta(models.Model):

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(
        max_length=200
    )

    texto = models.TextField()

    cidade = models.CharField(
        max_length=100
    )

    estado = models.CharField(
        max_length=100
    )

    imagem = models.ImageField(
        upload_to='cartas/',
        blank=True,
        null=True
    )

    adotado = models.BooleanField(
        default=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    correspondido = models.BooleanField(
        default=False
    )

    @property
    def adocao(self):

        return Adocao.objects.filter(
            carta=self
        ).first()

    def __str__(self):

        return self.titulo
    
class Curtida(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    carta = models.ForeignKey(
        Carta,
        on_delete=models.CASCADE,
        related_name='curtidas'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            'usuario',
            'carta'
        )

    def __str__(self):

        return f'{self.usuario} curtiu {self.carta}'
    
class Comentario(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    carta = models.ForeignKey(
        Carta,
        on_delete=models.CASCADE
    )

    texto = models.TextField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f'{self.usuario} comentou'
    
class Adocao(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    carta = models.OneToOneField(
        Carta,
        on_delete=models.CASCADE
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f'{self.usuario} adotou {self.carta}'
    
class Notificacao(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    mensagem = models.CharField(
        max_length=255
    )

    lida = models.BooleanField(
        default=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.mensagem
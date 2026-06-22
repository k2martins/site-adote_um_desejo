from django.contrib import admin

from .models import (
    Carta,
    Curtida,
    Comentario,
    Adocao,
    Notificacao
)

admin.site.register(Carta)
admin.site.register(Curtida)
admin.site.register(Comentario)
admin.site.register(Adocao)
admin.site.register(Notificacao)
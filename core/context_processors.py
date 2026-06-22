from cartas.models import Notificacao


def notificacoes(request):

    if request.user.is_authenticated:

        notificacoes_recentes = Notificacao.objects.filter(
            usuario=request.user
        ).order_by(
            '-criado_em'
        )[:5]

    else:

        notificacoes_recentes = []

    return {
        'notificacoes_recentes':
        notificacoes_recentes
    }
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    # CORE
    path(
        '',
        include('core.urls')
    ),

    # USUÁRIOS
    path(
        'usuarios/',
        include('usuarios.urls')
    ),

    # CARTAS
    path(
        'cartas/',
        include('cartas.urls')
    ),

    # RESET DE SENHA
    path(
        'senha-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='senha_reset.html'
        ),
        name='password_reset'
    ),

    path(
        'senha-reset-enviado/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='senha_reset_enviado.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='nova_senha.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'senha-reset-completo/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='senha_reset_completo.html'
        ),
        name='password_reset_complete'
    ),

]

# STATIC
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS[0]
)

# MEDIA
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),

    path('perfil/', views.perfil, name='perfil'),
    path(
        'editar-perfil/',
        views.editar_perfil,
        name='editar_perfil'
    ),
    path(
        'perfil/<str:username>/',
        views.perfil_publico,
        name='perfil_publico'
    ),
]
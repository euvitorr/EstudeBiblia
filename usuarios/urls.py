from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('perfil/', views.atualizar_perfil_view, name='atualizar_perfil'),
    path('logout/', views.logout_view, name='logout'), 
]

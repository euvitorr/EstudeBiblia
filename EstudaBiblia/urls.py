from django.conf.urls import url
from django.contrib import admin
from django.urls import path  # Importando path para usar no lugar de url, se você estiver usando Django >= 2.0

from biblia import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Rota sem parâmetros: usar valores padrão
    # Rota com parâmetros
    path('', views.home, name='home_without_params'),
    path('<str:id_livro>/<int:id_capitulo>/', views.home, name='home_with_params'),
    path('<str:id_livro>', views.home, name='home_without_cap'),
    path('<str:id_livro>/<int:id_capitulo>/create_note/', views.salvar_nota, name='create_note'),
    # Adicionando novas URLs para API AJAX
    path('api/livros/', views.livros_list, name='api_livros'),
    path('api/livros/<str:id_livro>/capitulos/', views.capitulos_por_livro, name='api_capitulos_por_livro'),
    path('api/livros/<str:id_livro>/capitulos/<int:id_capitulo>/versiculos/', views.versiculos_por_capitulo, name='api_versiculos_por_capitulo'),
]

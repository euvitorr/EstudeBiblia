from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'nome','email', 'rua', 'numero', 'cidade', 'estado', 'cep', 'is_staff']
    # Aqui redefinimos os fieldsets
    fieldsets = (
        ('Dados de Login', {'fields': ('username', 'password')}),
        ('Dados de Cadastro', {'fields': ('nome','email','foto_perfil', 'data_nascimento', 'rua', 'numero', 'cidade', 'estado', 'cep')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Não esqueça de ajustar os add_fieldsets se você também quiser customizar a página de "add user"
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Informações Adicionais', {'fields': ('nome','email','foto_perfil', 'data_nascimento', 'rua', 'numero', 'cidade', 'estado', 'cep')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

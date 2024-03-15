from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'rua', 'numero', 'cidade', 'estado', 'cep', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('foto_perfil', 'data_nascimento', 'rua', 'numero', 'cidade', 'estado', 'cep')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('foto_perfil', 'data_nascimento', 'rua', 'numero', 'cidade', 'estado', 'cep')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

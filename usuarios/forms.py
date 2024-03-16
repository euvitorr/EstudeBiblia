from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

# Substitua 'get_user_model()' por 'CustomUser' diretamente se você não está usando o modelo personalizado em AUTH_USER_MODEL
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nome', 'data_nascimento', 'foto_perfil', 'rua', 'numero', 'cidade', 'estado', 'cep',)
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'nome', 'data_nascimento', 'foto_perfil', 'rua', 'numero', 'cidade', 'estado', 'cep']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'w-full px-3 py-2 mt-1 border rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'})

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email', 'nome', 'data_nascimento', 'foto_perfil', 'rua', 'numero', 'cidade', 'estado', 'cep',)
        
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'nome', 'data_nascimento', 'foto_perfil', 'rua', 'numero', 'cidade', 'estado', 'cep']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'w-full px-3 py-2 mt-1 border rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'})

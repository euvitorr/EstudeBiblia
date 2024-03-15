from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfis/', null=True, blank=True)
    
    # Redefinir campos para evitar conflito
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",
        related_query_name="user",
    )
    nome = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=20, null=True, blank=True)


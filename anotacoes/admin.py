from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Campos que serão exibidos na lista de anotações
    search_fields = ('title', 'content')  # Campos pesquisáveis na interface de admin

admin.site.register(Note, NoteAdmin)

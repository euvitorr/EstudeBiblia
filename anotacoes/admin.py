from django.contrib import admin
from .models import Note, AnnotationRange

class AnnotationRangeInline(admin.TabularInline):
    model = AnnotationRange
    extra = 1  # Define quantos formulários de intervalos estarão disponíveis por padrão

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Campos que serão exibidos na lista de anotações
    search_fields = ('title', 'content')  # Campos pesquisáveis na interface de admin
    inlines = [AnnotationRangeInline]  # Permite editar os intervalos de versículos diretamente na anotação

admin.site.register(Note, NoteAdmin)

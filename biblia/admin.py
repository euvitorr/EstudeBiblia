from django.contrib import admin
from .models import Book, Chapter, Version, Verse

# Classe personalizada para o modelo Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')  # Exibe nome e ordem na listagem
    search_fields = ('name',)  # Permite buscar livros pelo nome

# Classe personalizada para o modelo Chapter
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'number')  # Exibe livro e número do capítulo
    search_fields = ('book__name',)  # Permite buscar capítulos pelo nome do livro
    list_filter = ('book',)  # Permite filtrar capítulos por livro

# Classe personalizada para o modelo Version
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Exibe o nome da versão
    search_fields = ('name',)  # Permite buscar versões pelo nome

# Classe personalizada para o modelo Verse
@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ('version', 'book', 'chapter', 'number', 'verse_preview')  # Exibe versão, livro, capítulo, número e uma prévia do verso
    search_fields = ('verse', 'book__name', 'version__name')  # Permite buscar versículos
    list_filter = ('book', 'version')  # Permite filtrar versículos por livro e versão

    def verse_preview(self, obj):
        return f"{obj.verse[:30]}..."  # Retorna os primeiros 30 caracteres do verso
    verse_preview.short_description = "Preview do Verso"  # Define o título da coluna no admin


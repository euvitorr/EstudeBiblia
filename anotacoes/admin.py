from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username')

    def get_queryset(self, request):
        """
        Sobrescreve o queryset padrão para limitar as anotações
        a serem exibidas apenas para as criadas pelo usuário logado,
        a menos que o usuário seja um superusuário.
        """
        qs = super(NoteAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Limita as opções de usuário para o usuário atual no formulário,
        a menos que seja um superusuário.
        """
        if db_field.name == "user" and not request.user.is_superuser:
            kwargs["queryset"] = Note.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Note, NoteAdmin)

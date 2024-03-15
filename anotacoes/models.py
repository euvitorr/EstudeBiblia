from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()  # Armazena HTML
    version = models.ForeignKey('biblia.Version', on_delete=models.CASCADE, null=True)  # Importação do app 'biblia'
    book = models.ForeignKey('biblia.Book', on_delete=models.CASCADE, related_name='start_ranges', null=True)
    chapter = models.ForeignKey('biblia.Chapter', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title


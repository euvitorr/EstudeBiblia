from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Armazena HTML
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title

class AnnotationRange(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='ranges')
    version = models.ForeignKey('biblia.Version', on_delete=models.CASCADE)  # Importação do app 'biblia'
    start_book = models.ForeignKey('biblia.Book', on_delete=models.CASCADE, related_name='start_ranges')
    start_chapter = models.IntegerField()
    start_verse = models.IntegerField()
    end_book = models.ForeignKey('biblia.Book', on_delete=models.CASCADE, related_name='end_ranges')
    end_chapter = models.IntegerField()
    end_verse = models.IntegerField()

    def __str__(self):
        return f"{self.start_book.name} {self.start_chapter}:{self.start_verse} - {self.end_book.name} {self.end_chapter}:{self.end_verse}"

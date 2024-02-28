from django.db import models
from django.db.models import Q, CheckConstraint

class Book(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)
    order = models.IntegerField(unique=True,null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order'] 

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    number = models.IntegerField()

    def __str__(self):
        return f"{self.book.name} - Capítulo {self.number}"

class Version(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)
    # Supondo que você tenha mais campos aqui, ajuste conforme necessário

    def __str__(self):
        return self.name


class Verse(models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='verses')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='verses')
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='verses', null=True) 
    number = models.IntegerField()
    verse = models.TextField()

    class Meta:
        constraints = [
            CheckConstraint(check=Q(book=('chapter__book')), name='chapter_belongs_to_book')
        ]

    def __str__(self):
        return f"{self.book.name} {self.chapter.number}:{self.number} - {self.verse[:30]}..."

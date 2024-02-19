from django.db import models

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
    chapter = models.IntegerField()
    number = models.IntegerField()
    verse = models.TextField()

    def __str__(self):
        return f"{self.book.name} {self.chapter}:{self.number} - {self.verse[:30]}..."

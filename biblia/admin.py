from django.contrib import admin
from .models import Book, Chapter, Version, Verse

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Version)
admin.site.register(Verse)

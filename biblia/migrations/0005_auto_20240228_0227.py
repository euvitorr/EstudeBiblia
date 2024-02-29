# Generated by Django 3.2.24 on 2024-02-28 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblia', '0004_alter_verse_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verses', to='biblia.chapter'),
        ),
        migrations.AddConstraint(
            model_name='verse',
            constraint=models.CheckConstraint(check=models.Q(('book', 'chapter__book')), name='chapter_belongs_to_book'),
        ),
    ]
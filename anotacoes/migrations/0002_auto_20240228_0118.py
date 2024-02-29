# Generated by Django 3.2.24 on 2024-02-28 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblia', '0003_auto_20240218_0324'),
        ('anotacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_ranges', to='biblia.book'),
        ),
        migrations.AddField(
            model_name='note',
            name='chapter',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblia.version'),
        ),
        migrations.DeleteModel(
            name='AnnotationRange',
        ),
    ]
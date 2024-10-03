from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

def set_default_user(apps, schema_editor):
    Note = apps.get_model('anotacoes', 'Note')
    User = apps.get_model(settings.AUTH_USER_MODEL.split('.')[0], settings.AUTH_USER_MODEL.split('.')[1])
    default_user = User.objects.first()
    if default_user:
        Note.objects.filter(user__isnull=True).update(user=default_user)

class Migration(migrations.Migration):

    dependencies = [
        ('anotacoes', '0004_note_user'),
    ]

    operations = [
        migrations.RunPython(set_default_user),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

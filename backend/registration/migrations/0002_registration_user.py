<<<<<<< HEAD
# Generated by Django 3.1.7 on 2021-03-24 14:16
=======
# Generated by Django 3.1.7 on 2021-03-24 10:43
>>>>>>> dev

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='registration', to=settings.AUTH_USER_MODEL),
        ),
    ]

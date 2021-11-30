# Generated by Django 3.2.7 on 2021-11-20 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codepartner', '0018_alter_session_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='book',
        ),
        migrations.AddField(
            model_name='session',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='session_book', to=settings.AUTH_USER_MODEL),
        ),
    ]
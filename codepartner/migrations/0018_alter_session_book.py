# Generated by Django 3.2.7 on 2021-11-20 10:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codepartner', '0017_auto_20211120_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='book',
            field=models.ManyToManyField(blank=True, related_name='session_book', to=settings.AUTH_USER_MODEL),
        ),
    ]

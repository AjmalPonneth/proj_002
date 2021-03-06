# Generated by Django 3.2.7 on 2021-11-17 06:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codepartner', '0012_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='thumbs',
            field=models.ManyToManyField(blank=True, default=None, related_name='comment_thumbs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='thumbsdown',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='comment',
            name='thumbsup',
            field=models.IntegerField(default='0'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepartner', '0009_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]

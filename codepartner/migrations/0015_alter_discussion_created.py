# Generated by Django 3.2.7 on 2021-11-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepartner', '0014_commentvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20211011_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='current_project',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_newuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
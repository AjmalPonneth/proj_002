# Generated by Django 3.2.7 on 2021-11-14 16:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codepartner', '0007_alter_session_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['user']},
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=100)),
                ('sub_category', models.CharField(choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('C', 'C'), ('C#', 'C#'), ('C++', 'C++'), ('Java', 'Java'), ('PHP', 'PHP'), ('GO', 'GO'), ('R', 'R'), ('Ruby', 'Ruby')], max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('thumpsup', models.IntegerField(default='0')),
                ('thumpsdown', models.IntegerField(default='0')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('thumbs', models.ManyToManyField(blank=True, default=None, related_name='thumbs', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

from django.db import models
from accounts.models import NewUser
from ckeditor.fields import RichTextField
# Create your models here.


class UserSkills(models.Model):
    user = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, blank=True, null=True)
    python = models.BooleanField(default=False, blank=True)
    javascript = models.BooleanField(default=False, blank=True)
    php = models.BooleanField(default=False, blank=True)
    java = models.BooleanField(default=False, blank=True)
    cpp = models.BooleanField(default=False, blank=True)
    csharp = models.BooleanField(default=False, blank=True)
    ruby = models.BooleanField(default=False, blank=True)
    go = models.BooleanField(default=False, blank=True)
    r = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user.email


class Session(models.Model):
    goal_choices = (
        ('Self-Study', 'Self-Study'),
        ('Interview Prepration', 'Interview Prepration'),
        ('Competitive Programming', 'Competitive Programming'),
        ('Newbie Coding', 'Newbie Coding'),
        ('Knowledge Sharing', 'Knowledge Sharing'),
        ('Other', 'Other'),
    )
    language_choices = (
        ('Python', 'Python'),
        ('Javascript', 'Javascript'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('PHP', 'PHP'),
        ('R', 'R'),
        ('Go', 'Go'),
        ('Other', 'Other'),
    )
    level_choices = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    user = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name="session_creator", blank=False)
    book = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name="session_book", blank=True, null=True)
    goal = models.CharField(blank=False, max_length=100, choices=goal_choices)
    language = models.CharField(
        blank=False, max_length=100, choices=language_choices)
    level = models.CharField(
        blank=False, max_length=100, choices=level_choices)
    desc = models.TextField(blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -- {}".format(self.language, self.level)

    class Meta:
        ordering = ['user']


class Discussion(models.Model):
    category_choices = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    sub_category_choices = (
        ('Python', 'Python'),
        ('Javascript', 'Javascript'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('PHP', 'PHP'),
        ('GO', 'GO'),
        ('R', 'R'),
        ('Ruby', 'Ruby'),
    )
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=250)
    category = models.CharField(
        blank=False, max_length=100, choices=category_choices)
    sub_category = models.CharField(
        max_length=100, choices=sub_category_choices)
    content = RichTextField()
    thumpsup = models.IntegerField(default='0')
    thumpsdown = models.IntegerField(default='0')
    thumbs = models.ManyToManyField(
        NewUser, related_name='thumbs', default=None, blank=True)
    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user}"


class Vote(models.Model):
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name='disid', default=None, blank=True)
    user = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name='userid', default=None, blank=True)
    vote = models.BooleanField(default=True)

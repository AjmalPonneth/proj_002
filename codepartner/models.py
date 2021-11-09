from django.db import models
from accounts.models import NewUser
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

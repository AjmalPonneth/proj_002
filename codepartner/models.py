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

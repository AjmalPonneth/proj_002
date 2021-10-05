from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, first_name, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        return self.create_user(email, first_name, username, password, **other_fields)

    def create_user(self, email, username, phone_number, password, **otherfields):
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    startdate = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=10, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_newuser = models.BooleanField(default=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']


@receiver(post_save, sender=NewUser)
def register_user(sender, instance, created, **kwargs):
    if created:
        subject = 'Codepartner'
        message = 'Hello! This is from codepartner, Your account crerated successfully!'
        to = instance
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [to], fail_silently=False)

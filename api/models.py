from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    role = models.CharField(choices=(('scholar', 'Scholar'), ('instructor', 'Instructor'), ('moderator', 'Moderator')), max_length=12)
    credit = models.PositiveIntegerField(default=0)
    courses = models.JSONField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


def add_user_to_group(sender, instance, created, **kwargs):
    """Post-create user signal that adds the user to everyone group."""

    try:
        if created:
            if instance.role is 'instructor':
                instance.groups.add(Group.objects.get(pk=3))
            else:
                instance.groups.add(Group.objects.get(pk=4))
    except Group.DoesNotExist:
        pass

post_save.connect(add_user_to_group, sender=User)
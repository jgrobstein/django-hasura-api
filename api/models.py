from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Role(models.Model):
    is_moderator = 1
    is_instructor = 2
    is_scholar = 3
    active_roles=(
        (is_moderator, "Moderator"),
        (is_instructor, "Instructor"),
        (is_scholar, "Scholar"),
    )
    id = models.PositiveIntegerField(choices=active_roles, primary_key=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    courses= models.JSONField(null=True, blank=True)

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
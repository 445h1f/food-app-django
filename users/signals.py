from django.db.models.signals import post_save # sender
from django.contrib.auth.models import User # instance
from django.dispatch import receiver # reciever
from .models import Profile # profile to be created


# triggers when user submits registration form
@receiver(signal=post_save, sender=User)
def buildProfile(sender, instance, created, **kwargs):
    # building user profile if created
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    #saving profile
    instance.profile.save()
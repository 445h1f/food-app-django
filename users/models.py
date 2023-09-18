from django.db import models
from django.contrib.auth.models import User

# extending django inbuilt User data model
class Profile(models.Model):
    # one to one relationship with profile and user
    # means one user has one profile
    # on_delete=models.CASCADE will delete profile also if user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default="default_profile.jpg", upload_to="profile_pictures")
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
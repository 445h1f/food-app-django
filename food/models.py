from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=10240)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(
        max_length=1024, default='https://nayemdevs.com/wp-content/uploads/2020/03/default-product-image.png')
    # referencing which user has created item by adding user field as foreign key
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)

    # method to redirect on detail page after Item is created
    def get_absolute_url(self):
        # returns detail view of item with pk as passed in view
        return reverse(viewname='food:details', kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name

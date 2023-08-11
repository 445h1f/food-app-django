from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=10240)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=1024, default='https://nayemdevs.com/wp-content/uploads/2020/03/default-product-image.png')

    def __str__(self) -> str:
        return self.name
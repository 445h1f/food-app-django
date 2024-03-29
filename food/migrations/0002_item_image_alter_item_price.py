# Generated by Django 4.2.4 on 2023-08-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://nayemdevs.com/wp-content/uploads/2020/03/default-product-image.png', max_length=1024),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_image_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=10240),
        ),
    ]

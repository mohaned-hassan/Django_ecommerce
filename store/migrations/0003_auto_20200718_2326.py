# Generated by Django 3.0.8 on 2020-07-18 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OdrderItem',
            new_name='OrderItem',
        ),
    ]

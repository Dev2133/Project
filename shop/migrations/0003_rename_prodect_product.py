# Generated by Django 5.1.1 on 2024-10-11 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_prodect_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prodect',
            new_name='Product',
        ),
    ]
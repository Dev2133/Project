# Generated by Django 5.1.1 on 2024-10-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodect',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

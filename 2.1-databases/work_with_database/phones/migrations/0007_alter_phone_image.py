# Generated by Django 5.0.2 on 2024-03-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='phones/', verbose_name='Image'),
        ),
    ]

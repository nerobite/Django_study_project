# Generated by Django 5.0.2 on 2024-03-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, upload_to='phones/'),
        ),
    ]

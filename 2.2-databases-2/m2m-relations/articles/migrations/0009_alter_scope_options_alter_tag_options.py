# Generated by Django 5.0.2 on 2024-03-17 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_раздел_scope_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'ТЕМАТИКИ СТАТЬИ', 'verbose_name_plural': 'ТЕМАТИКИ СТАТЕЙ'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'РАЗДЕЛ', 'verbose_name_plural': 'РАЗДЕЛЫ'},
        ),
    ]

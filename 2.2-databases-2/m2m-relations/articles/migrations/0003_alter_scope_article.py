# Generated by Django 5.0.2 on 2024-03-17 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_scopes', to='articles.article'),
        ),
    ]

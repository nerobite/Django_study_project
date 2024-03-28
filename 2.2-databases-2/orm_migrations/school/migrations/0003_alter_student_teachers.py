# Generated by Django 5.0.2 on 2024-03-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher', verbose_name='Учителя'),
        ),
    ]
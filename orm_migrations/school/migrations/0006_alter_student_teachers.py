# Generated by Django 5.0.7 on 2024-07-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
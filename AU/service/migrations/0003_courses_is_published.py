# Generated by Django 3.1.1 on 2021-05-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_courses_course_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image_name', models.CharField(max_length=200)),
                ('slider_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]

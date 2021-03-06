# Generated by Django 3.1.1 on 2021-05-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(blank=True, max_length=200)),
                ('hero_img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('about_img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('seo_tag', models.CharField(blank=True, max_length=100)),
                ('about_description', models.TextField(blank=True)),
                ('about_description_sub', models.TextField(blank=True)),
                ('about_description_sub_I', models.TextField(blank=True)),
            ],
        ),
    ]

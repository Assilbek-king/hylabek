# Generated by Django 4.0.4 on 2023-02-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_photo_description_photo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
                ('mini_description', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]

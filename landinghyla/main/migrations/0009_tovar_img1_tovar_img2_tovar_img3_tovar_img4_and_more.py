# Generated by Django 4.0.4 on 2022-12-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_otziv'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='img1',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='img2',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='img3',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='img4',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='img5',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]
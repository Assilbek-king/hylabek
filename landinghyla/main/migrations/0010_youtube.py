# Generated by Django 4.0.4 on 2022-12-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_tovar_img1_tovar_img2_tovar_img3_tovar_img4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('link', models.TextField(blank=True)),
            ],
        ),
    ]

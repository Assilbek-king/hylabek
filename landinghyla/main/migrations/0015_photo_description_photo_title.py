# Generated by Django 4.0.4 on 2023-02-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_category_kztitle_remove_feedback_categoriya_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]

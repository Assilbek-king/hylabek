# Generated by Django 4.0.4 on 2022-12-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_lang_delete_link_category_lang_otziv_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='otziv',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='otziv',
            name='status',
        ),
        migrations.AddField(
            model_name='category',
            name='kztitle',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='otziv',
            name='kzcomment',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.DeleteModel(
            name='Lang',
        ),
    ]

# Generated by Django 4.0.4 on 2023-02-01 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_category_lang_remove_otziv_lang_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='kztitle',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='categoriya',
        ),
        migrations.RemoveField(
            model_name='otziv',
            name='kzcomment',
        ),
        migrations.RemoveField(
            model_name='tovar',
            name='interyer',
        ),
    ]

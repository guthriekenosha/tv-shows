# Generated by Django 3.2.5 on 2021-07-18 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0003_show_descirption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='descirption',
            new_name='description',
        ),
    ]

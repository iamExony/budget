# Generated by Django 4.0.6 on 2022-07-07 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='thecurrency',
            new_name='the_currency',
        ),
        migrations.RenameField(
            model_name='budget',
            old_name='theduration',
            new_name='the_duration',
        ),
    ]

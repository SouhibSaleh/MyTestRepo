# Generated by Django 5.0.6 on 2024-07-04 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myitem',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='myitem',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='myitem',
            old_name='Name',
            new_name='name',
        ),
    ]

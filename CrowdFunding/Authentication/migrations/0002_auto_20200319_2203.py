# Generated by Django 3.0.4 on 2020-03-19 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='Last_name',
            new_name='last_name',
        ),
    ]
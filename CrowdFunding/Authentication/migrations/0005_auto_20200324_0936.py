# Generated by Django 3.0.4 on 2020-03-24 07:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0004_merge_20200322_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-24 10:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile_page', '0005_remove_post_id_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]

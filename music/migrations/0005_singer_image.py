# Generated by Django 5.2.4 on 2025-07-15 09:11

import music.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0004_tag_alter_song_id_singer_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="singer",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=music.models.image_upload_path
            ),
        ),
    ]

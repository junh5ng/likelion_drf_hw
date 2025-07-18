# Generated by Django 5.2.4 on 2025-07-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0003_song"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="song",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name="singer",
            name="tags",
            field=models.ManyToManyField(blank=True, to="music.tag"),
        ),
    ]

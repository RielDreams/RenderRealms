# Generated by Django 4.1.5 on 2023-02-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_cars_description_cars_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="buildings",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="buildings",
            name="file",
            field=models.FileField(default=1, upload_to="blender_files/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="characters",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="characters",
            name="file",
            field=models.FileField(default=1, upload_to="blender_files/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="environments",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="environments",
            name="file",
            field=models.FileField(default=1, upload_to="blender_files/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cars",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]

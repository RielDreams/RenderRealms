# Generated by Django 4.1.5 on 2023-02-10 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0008_rename_photo_url_cars_photo_remove_cars_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cars",
            old_name="photo",
            new_name="photo_url",
        ),
    ]
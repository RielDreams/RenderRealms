# Generated by Django 4.1.5 on 2023-02-12 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0012_rename_character_projects_characters_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="characters",
            name="url",
        ),
    ]
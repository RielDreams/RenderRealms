# Generated by Django 4.1.5 on 2023-02-10 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0005_remove_editbuildings_building_remove_cars_file_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name="editcharacters",
            name="project",
        ),
        migrations.AddField(
            model_name="cars",
            name="photo_url",
            field=models.ImageField(blank=True, null=True, upload_to="car_photos/"),
        ),
        migrations.AddField(
            model_name="editcharacters",
            name="character",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.characters",
            ),
            preserve_default=False,
        ),
    ]

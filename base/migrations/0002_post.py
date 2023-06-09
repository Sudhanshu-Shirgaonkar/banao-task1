# Generated by Django 4.1.7 on 2023-03-14 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=20)),
                ("post_image", models.ImageField(upload_to="post_pics")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Mental Health", "MENTAL HEALTH"),
                            ("Heart Disease", "HEART DESEASE"),
                            ("Covid 19", "COVID 19"),
                            ("Immunization", "IMMUNIZATION"),
                        ],
                        default="Mental Halth",
                        max_length=100,
                    ),
                ),
                ("summary", models.TextField()),
                ("content", models.TextField()),
                ("is_draft", models.BooleanField(default=False)),
                ("is_saved", models.BooleanField(default=False)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-created"],},
        ),
    ]

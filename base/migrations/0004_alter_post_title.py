# Generated by Django 4.1.7 on 2023-03-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_post_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="title", field=models.CharField(max_length=100),
        ),
    ]

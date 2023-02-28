# Generated by Django 4.1.2 on 2023-01-25 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0005_rename_pic4_buyer_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainApp.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainApp.buyer"
                    ),
                ),
            ],
        ),
    ]

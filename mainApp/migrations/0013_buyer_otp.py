# Generated by Django 4.1.2 on 2023-02-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0012_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="buyer", name="otp", field=models.IntegerField(default=-1151515),
        ),
    ]

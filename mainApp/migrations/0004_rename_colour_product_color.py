# Generated by Django 4.1.2 on 2022-11-12 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0003_rename_finalprise_product_finalprice"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="colour", new_name="color",
        ),
    ]

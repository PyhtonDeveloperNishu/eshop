# Generated by Django 4.1.2 on 2022-11-09 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0002_alter_buyer_pic4_alter_product_pic1_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="finalprise", new_name="finalprice",
        ),
    ]

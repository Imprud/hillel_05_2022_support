# Generated by Django 4.0.6 on 2022-08-03 18:23

from django.db import migrations
from apps.authentication.services import create_dev_user


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_auto_20220803_1823"),
    ]

    operations = [migrations.RunPython(create_dev_user)]
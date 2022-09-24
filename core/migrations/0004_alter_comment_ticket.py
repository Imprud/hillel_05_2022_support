# Generated by Django 4.0.6 on 2022-09-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_comment_reply_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="ticket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="core.ticket",
            ),
        ),
    ]

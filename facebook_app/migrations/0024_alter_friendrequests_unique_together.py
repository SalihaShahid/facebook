# Generated by Django 4.2.3 on 2023-07-27 16:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facebook_app", "0023_textstorylike_textstorycomment_mediastorylike_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="friendrequests",
            unique_together=set(),
        ),
    ]
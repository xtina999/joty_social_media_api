# Generated by Django 5.0.6 on 2024-05-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(null=True),
        ),
    ]

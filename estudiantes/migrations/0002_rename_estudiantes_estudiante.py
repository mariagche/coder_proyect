# Generated by Django 4.1.4 on 2023-01-03 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("estudiantes", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Estudiantes",
            new_name="Estudiante",
        ),
    ]

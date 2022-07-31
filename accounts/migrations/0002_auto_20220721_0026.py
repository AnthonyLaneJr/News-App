# Generated by Django 4.0.6 on 2022-07-21 00:26

from django.db import migrations


def populate_roles(apps, schemaeditor):
    roles = {
        "reader":"A reader of the newspaper.",
        "journalist":"A user that works at the newspaper as a content creator",
        "columnist":"A user that writes content for a column",
        "editor":"A person tasked with reviewing jounralist work prior to publishing"
    }
    Role = apps.get_model("accounts", "Role")
    for name, desc in roles.items():
        role_obj = Role(name=name, description=desc)
        role_obj.save()


def populate_departments(apps, schemaeditor):
    departments = {
        "front_page":"A department tasked with writing the front page articles",
        "sports": "A department tasked with writing sports articles",
        "society":"A department tasked with writing society related articles",
        "business":"A department tasked with writing business related articles",
        "politics":"A deparmtent tasked with writing politics related articles",
        "classifieds":"A department tasked with reviewing and publishing classified ads"
    }
    Department = apps.get_model("accounts", "Department")
    for name, desc in departments.items():
        role_obj = Department(name=name, description=desc)
        role_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_departments),
        migrations.RunPython(populate_roles),
    ]

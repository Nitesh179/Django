# Generated by Django 4.2 on 2023-04-18 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Xmen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date',
            new_name='dob',
        ),
    ]

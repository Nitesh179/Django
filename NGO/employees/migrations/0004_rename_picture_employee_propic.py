# Generated by Django 4.2 on 2023-04-28 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='picture',
            new_name='propic',
        ),
    ]

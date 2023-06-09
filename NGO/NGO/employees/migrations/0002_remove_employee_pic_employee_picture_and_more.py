# Generated by Django 4.2 on 2023-04-28 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='pic',
        ),
        migrations.AddField(
            model_name='employee',
            name='picture',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ifsc',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]

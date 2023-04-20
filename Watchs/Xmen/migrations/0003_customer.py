# Generated by Django 4.2 on 2023-04-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Xmen', '0002_rename_date_contact_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.CharField()),
            ],
        ),
    ]

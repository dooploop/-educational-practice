# Generated by Django 3.1.7 on 2023-04-10 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0003_members_cores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='cores',
        ),
    ]

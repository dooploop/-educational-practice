# Generated by Django 3.1.7 on 2023-04-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0005_all_users_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_users_data',
            name='program_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

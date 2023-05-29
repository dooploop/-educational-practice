# Generated by Django 3.1.7 on 2023-04-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0006_all_users_data_program_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_users_data',
            name='memory_usage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_users_data',
            name='n_threads',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_users_data',
            name='status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
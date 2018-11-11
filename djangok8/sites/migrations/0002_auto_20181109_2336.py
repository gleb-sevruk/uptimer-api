# Generated by Django 2.1.3 on 2018-11-09 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='url',
            new_name='site_url',
        ),
        migrations.AlterField(
            model_name='site',
            name='last_check_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 9, 23, 36, 2, 157366)),
        ),
        migrations.AlterField(
            model_name='site',
            name='status',
            field=models.CharField(default='created', max_length=200),
        ),
    ]

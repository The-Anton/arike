# Generated by Django 4.0.1 on 2022-03-07 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_note_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 7, 16, 0, 7, 578766)),
        ),
    ]

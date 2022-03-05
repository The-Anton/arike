# Generated by Django 4.0.1 on 2022-03-04 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='given_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.visit'),
        ),
        migrations.AddField(
            model_name='health_info',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.visit'),
        ),
    ]
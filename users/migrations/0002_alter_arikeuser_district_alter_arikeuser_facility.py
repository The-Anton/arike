# Generated by Django 4.0.1 on 2022-03-05 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arikeuser',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facility.district'),
        ),
        migrations.AlterField(
            model_name='arikeuser',
            name='facility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facility.facility'),
        ),
    ]

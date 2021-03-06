# Generated by Django 4.0.1 on 2022-03-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LSG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[(1, 'Grama Panchayath'), (2, 'Block Panchayath'), (3, 'District Panchayath'), (4, 'Nagar Panchayath'), (10, 'Municipality'), (20, 'Corporation'), (50, 'Others')], max_length=100)),
                ('lsg_body_code', models.CharField(choices=[(1, 'Grama Panchayath'), (2, 'Block Panchayath'), (3, 'District Panchayath'), (4, 'Nagar Panchayath'), (10, 'Municipality'), (20, 'Corporation'), (50, 'Others')], max_length=100)),
                ('discrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.district')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('lsg_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.lsg')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('pin_code', models.IntegerField(max_length=6)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('kind', models.CharField(choices=[('PHC', 'PHC'), ('CHC', 'CHC')], default='PHC', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.ward')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.state'),
        ),
    ]

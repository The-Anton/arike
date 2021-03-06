# Generated by Django 4.0.1 on 2022-03-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('email', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('emergency_phone_number', models.IntegerField(max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.facility')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.ward')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=1000)),
                ('care_type', models.CharField(choices=[('General care', 'General care'), ('Genito urinary care', 'Genito urinary care'), ('Gastro-intestinal care', 'Gastro-intestinal care')], max_length=100)),
                ('care_sub_type', models.CharField(choices=[('Mouth care', 'Mouth care'), ('Bath', 'Bath'), ('Nail cutting', 'Nail cutting'), ('Shaving', 'Shaving')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.disease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('relation', models.CharField(choices=[('BROTHER', 'BROTHER'), ('SISTER', 'SISTER'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('FATHER', 'FATHER'), ('MOTHER', 'MOTHER'), ('HUSBAND', 'HUSBAND'), ('WIFE', 'WIFE')], max_length=100)),
                ('education', models.CharField(choices=[('BELOW HIGH SCHOOL', 'BELOW HIGH SCHOOL'), ('HIGH SCHOOL', 'HIGH SCHOOL'), ('SECONDARY HIGH SCHOOL', 'SECONDARY HIGH SCHOOL'), ('BACHELOR', 'BACHELOR'), ('MASTERS', 'MASTERS'), ('PHD', 'PHD')], max_length=100)),
                ('occupation', models.CharField(max_length=50, null=True)),
                ('is_primary', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
    ]

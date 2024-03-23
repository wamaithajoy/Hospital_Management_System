# Generated by Django 4.2.11 on 2024-03-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeHealthService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('contact_information', models.CharField(max_length=100)),
                ('physical_address', models.TextField()),
                ('service_requested', models.CharField(choices=[('Nursing', 'Nursing'), ('Therapy', 'Therapy')], max_length=50)),
                ('medical_history', models.TextField()),
                ('emergency_contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VirtualConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('reason_for_consultation', models.TextField()),
                ('preferred_datetime', models.DateTimeField()),
            ],
        ),
    ]
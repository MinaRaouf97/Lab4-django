# Generated by Django 4.0.1 on 2022-01-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('intake_name', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('track_name', models.CharField(max_length=20)),
            ],
        ),
    ]

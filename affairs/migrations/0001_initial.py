# Generated by Django 4.0.1 on 2022-01-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_affairs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
    ]

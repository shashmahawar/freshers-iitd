# Generated by Django 4.1 on 2022-09-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('kerberos', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('hostel', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
    ]

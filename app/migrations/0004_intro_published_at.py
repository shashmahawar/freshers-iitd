# Generated by Django 4.1 on 2022-09-11 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_profile_hostel'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

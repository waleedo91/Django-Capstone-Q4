# Generated by Django 3.1.7 on 2021-04-12 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

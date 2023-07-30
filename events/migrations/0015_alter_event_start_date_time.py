# Generated by Django 3.2.20 on 2023-07-30 08:08

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_alter_event_start_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 7, 31, 8, 8, 28, 983891, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 8, 3, 8, 8, 28, 983906, tzinfo=utc))]),
        ),
    ]

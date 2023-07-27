# Generated by Django 3.2.20 on 2023-07-27 17:19

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_start_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 7, 28, 17, 19, 9, 972231, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 7, 31, 17, 19, 9, 972246, tzinfo=utc))]),
        ),
    ]

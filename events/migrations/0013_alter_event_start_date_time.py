# Generated by Django 3.2.20 on 2023-07-29 01:29

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20230728_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 7, 30, 1, 29, 37, 815952, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 8, 2, 1, 29, 37, 815966, tzinfo=utc))]),
        ),
    ]

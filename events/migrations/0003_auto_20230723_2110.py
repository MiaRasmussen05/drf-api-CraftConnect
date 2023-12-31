# Generated by Django 3.2.20 on 2023-07-23 21:10

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20230723_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 7, 24, 21, 10, 26, 526638, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 7, 27, 21, 10, 26, 526654, tzinfo=utc))]),
        ),
    ]

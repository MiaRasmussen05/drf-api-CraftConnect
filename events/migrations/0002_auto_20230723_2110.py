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
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 7, 24, 21, 10, 15, 274085, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 7, 27, 21, 10, 15, 274115, tzinfo=utc))]),
        ),
    ]

# Generated by Django 3.2.20 on 2023-07-26 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_event_start_date_time'),
        ('comments', '0002_comment_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]
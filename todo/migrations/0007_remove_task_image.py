# Generated by Django 3.2.20 on 2023-07-27 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_task_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
    ]

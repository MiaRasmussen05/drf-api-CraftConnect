# Generated by Django 3.2.20 on 2023-07-29 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_task_todos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='todos',
        ),
        migrations.CreateModel(
            name='TaskContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='todo.task')),
            ],
        ),
    ]

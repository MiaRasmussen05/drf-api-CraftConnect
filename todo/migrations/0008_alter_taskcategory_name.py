# Generated by Django 3.2.20 on 2023-07-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_remove_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]

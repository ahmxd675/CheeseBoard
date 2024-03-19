# Generated by Django 2.2.28 on 2024-03-19 23:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CheeseBoardSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountCreationDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 23, 25, 16, 262856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='dateLastLoggedIn',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 23, 25, 16, 262856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime(2024, 3, 19, 23, 25, 16, 262857)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timeDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 23, 25, 16, 265856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 23, 25, 16, 264356, tzinfo=utc)),
        ),
    ]

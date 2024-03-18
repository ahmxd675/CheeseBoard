# Generated by Django 2.2.28 on 2024-03-18 11:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CheeseBoardSite', '0008_auto_20240318_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountCreationDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 11, 59, 42, 700085, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='dateLastLoggedIn',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 11, 59, 42, 700085, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime(2024, 3, 18, 11, 59, 42, 700085)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timeDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 11, 59, 42, 703077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 11, 59, 42, 702082, tzinfo=utc)),
        ),
    ]

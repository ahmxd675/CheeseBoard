# Generated by Django 2.2.28 on 2024-03-16 20:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CheeseBoardSite', '0002_auto_20240315_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountCreationDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 20, 1, 39, 88783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='dateLastLoggedIn',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 20, 1, 39, 88783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime(2024, 3, 16, 20, 1, 39, 88784)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='account',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Account'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timeDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 20, 1, 39, 91783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='account',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Account'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(default='', max_length=265),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 20, 1, 39, 90283, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='saved',
            name='account',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Account'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='cheesesReferenced',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='commentsGiven',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='commentsTaken',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='likesGiven',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='likesTaken',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='posts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='timeOnCheeseBoard',
            field=models.IntegerField(default=0),
        ),
    ]

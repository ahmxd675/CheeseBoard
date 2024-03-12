# Generated by Django 2.2.28 on 2024-03-12 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=265)),
                ('body', models.CharField(max_length=4096)),
                ('likes', models.IntegerField()),
                ('timeDate', models.DateTimeField()),
                ('cheeses', models.ManyToManyField(blank=True, null=True, to='CheeseBoardSite.Cheese')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOnCheeseBoard', models.IntegerField()),
                ('posts', models.IntegerField()),
                ('likesTaken', models.IntegerField()),
                ('likesGiven', models.IntegerField()),
                ('commentsTaken', models.IntegerField()),
                ('commentsGiven', models.IntegerField()),
                ('cheesesReferenced', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('dateOfBirth', models.DateField()),
                ('accountCreationDate', models.DateTimeField()),
                ('dateLastLoggedIn', models.DateTimeField()),
                ('profilePic', models.ImageField(blank=True, upload_to='profile_images')),
                ('stats', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='CheeseBoardSite.Stats')),
                ('badges', models.ManyToManyField(blank=True, null=True, to='CheeseBoardSite.Badge')),
                ('faveCheese', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CheeseBoardSite.Cheese')),
                ('followers', models.ManyToManyField(blank=True, null=True, related_name='_account_followers_+', to='CheeseBoardSite.Account')),
                ('following', models.ManyToManyField(blank=True, null=True, related_name='_account_following_+', to='CheeseBoardSite.Account')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('posts', models.ManyToManyField(blank=True, null=True, to='CheeseBoardSite.Post')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Account')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Account'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('body', models.CharField(max_length=64)),
                ('timeDate', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Post')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CheeseBoardSite.Account')),
            ],
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Cheese(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class Stats(models.Model):
    ID = models.IntegerField(primary_key = True, default = 0)
    timeOnCheeseBoard = models.IntegerField(default = 0)
    posts  = models.IntegerField(default = 0)
    likesTaken = models.IntegerField(default = 0)
    likesGiven = models.IntegerField(default = 0)
    commentsTaken = models.IntegerField(default = 0)
    commentsGiven = models.IntegerField(default = 0)
    cheesesReferenced = models.IntegerField(default = 0)

    def __str__(self):
        return self.timeOnCheeseBoard

class Badge(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name
    
class Account(models.Model):
    #username, password, email, forename, surname in user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable = True)
    dateOfBirth = models.DateField(default = datetime.today())
    accountCreationDate = models.DateTimeField(default = timezone.now())
    dateLastLoggedIn = models.DateTimeField(default = timezone.now())
    profilePic = models.ImageField(upload_to='profile_images', blank=True)

    stats = models.OneToOneField(
        Stats,
        on_delete=models.CASCADE,
        primary_key = True,
    )
    faveCheese = models.ForeignKey(
        Cheese,
        on_delete=models.SET_NULL,
        null = True,
    )
    followers = models.ManyToManyField(
        'self',
        blank = True,
        null = True,
    )
    following = models.ManyToManyField(
        'self',
        blank = True,
        null = True,
    )
    badges = models.ManyToManyField(
        Badge,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.user.username

class Post(models.Model):
    ID = models.IntegerField(primary_key = True, default = 0)
    title = models.CharField(max_length = 64, default = "")
    image = models.ImageField(blank = True)
    caption = models.CharField(max_length = 265, default = "")
    body = models.CharField(max_length = 4096, default = "")
    likes = models.IntegerField(default = 0)
    timeDate = models.DateTimeField(default = timezone.now())
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True,
        default = "",
    )
    cheeses = models.ManyToManyField(
        Cheese,
        blank = True,
        null=True,
    )
    def __str__(self):
        return self.title

class Saved(models.Model):
    name = models.CharField(max_length = 64)
    posts= models.ManyToManyField(
        Post,
        blank=True,
        null=True,
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True,
        default = "",
    )
    def __str__(self):
        return self.name

class Comment(models.Model):
    ID = models.IntegerField(primary_key = True, default = 0)
    likes = models.IntegerField(default = 0)
    body = models.CharField(max_length = 64)
    timeDate = models.DateTimeField(default = timezone.now())
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null = True,
        default = "",
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null = True,
        default = "",
    )
    def __str__(self):
        return self.body
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cheese(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class Stats(models.Model):
    timeOnCheeseBoard = models.IntegerField()
    posts  = models.IntegerField()
    likesTaken = models.IntegerField()
    likesGiven = models.IntegerField()
    commentsTaken = models.IntegerField()
    commentsGiven = models.IntegerField()
    cheesesReferenced = models.IntegerField()

    def __str__(self):
        return self.timeOnCheeseBoard

class Badge(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name
    
class Account(models.Model):
    #username, password, email, forename, surname in user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dateOfBirth = models.DateField()
    accountCreationDate = models.DateTimeField()
    dateLastLoggedIn = models.DateTimeField()
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
        return self.username

class Post(models.Model):
    ID = models.IntegerField()
    title = models.CharField(max_length = 64)
    image = models.ImageField()
    caption = models.CharField(max_length = 265)
    body = models.CharField(max_length = 4096)
    likes = models.IntegerField()
    timeDate = models.DateTimeField()
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
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
    )
    def __str__(self):
        return self.name

class Comment(models.Model):
    likes = models.IntegerField()
    body = models.CharField(max_length = 64)
    timeDate = models.DateTimeField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.body
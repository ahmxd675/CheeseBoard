import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CheeseBoard.settings')
import django
django.setup()
import datetime
from django.db import models
from django.contrib.auth.models import User
from CheeseBoardSite.models import Account, Cheese, Badge, Saved, Post, Comment, Stats

def populate():
    
    cheese = [
        {"name" : "Cheddar"},
        {"name" : "Brie"},
        {"name" : "Halloumi"},
        {"name" : "Camenbert"},
        {"name" : "Edam"},
        {"name" : "Red Leister"},
        {"name" : "Wensleydale"},
        {"name" : "Gouda"},
        {"name" : "Jalsberg"},
        {"name" : "Mozzarella"},
        {"name" : "Gorgonzola"},
        {"name" : "Somerset-Brie"},
    ]

    stats = [
        {"ID" : 1,
        "timeOnCheeseBoard" : 17,
         "posts" : 0,
         "likesTaken" : 3,
         "likesGiven" : 4,
         "commentsTaken" : 0,
         "commentsGiven" : 2,
         "cheesesReferenced" : 0},
         {"ID" : 2,
        "timeOnCheeseBoard" : 182,
         "posts" : 4,
         "likesTaken" : 15,
         "likesGiven" : 2,
         "commentsTaken" : 3,
         "commentsGiven" : 1,
         "cheesesReferenced" : 5},
         {"ID" : 3,
        "timeOnCheeseBoard" : 52,
         "posts" : 1,
         "likesTaken" : 12,
         "likesGiven" : 2,
         "commentsTaken" : 1,
         "commentsGiven" : 1,
         "cheesesReferenced" : 2}
    ]

    badges = []

    account = [
        {"username" : "Carlie19",
         "password" : "carl.is.great",
         "email" : "carl@gmail.com",
         "forename" : "Carl",
         "surname" : "Marques",
        "dateOfBirth" : datetime.date(1977,10,19),
         "accountCreationDate" : datetime.date(2020,11,11),
         "dateLastLoggedIn" : datetime.date(2024,11,03),
         "profilePic" : "profile_images/Run.jpg",
         "stats" : 2,
         "faveCheese" : "Cheddar",
         "followers" : ["Steve", "Marge"],
         "following" : ["Steve"],
         "badges" : ["Ten Days", "Fifty Days", "One Hundred Days",
                     "You Posted!", "10 Likes", "You Commented!",
                     "You Referenced 5 Cheeses!"]},

         {"username" : "Marge",
         "password" : "3xDhE28.ye*",
         "email" : "Marge12@gmail.com",
         "forename" : "Margaret",
         "surname" : "Plumber",
        "dateOfBirth" : datetime.date(1953,11,12),
         "accountCreationDate" : datetime.date(2022,12,20),
         "dateLastLoggedIn" : datetime.date(2023,02,15),
         "profilePic" : "profile_images/Sit.jpg",
         "stats" : 1,
         "faveCheese" : "Red Leister",
         "followers" : [],
         "following" : ["Carlie19"],
         "badges" : ["Ten Days"]},

         {"username" : "Steve",
         "password" : "StevieTheSteveStevenson",
         "email" : "Steevo@gmail.com",
         "forename" : "Steve",
         "surname" : "Stevenson",
        "dateOfBirth" : datetime.date(1988,02,04),
         "accountCreationDate" : datetime.date(2023,06,23),
         "dateLastLoggedIn" : datetime.date(2024,09,03),
         "profilePic" : "profile_images/Suit.jpg",
         "stats" : 3,
         "faveCheese" : "Brie",
         "followers" : ["Carlie19"],
         "following" : ["Carlie19"],
         "badges" : ["Ten Days", "Fifty Days", "Ten Likes",
                     "You Posted!", "You Commented!"]},
    ]

    post = [
        {
            "ID" : 1,
            "title" : "First Post!!!",
            "image" : "PostImages/BOARD.jpg",
            "caption" : "I MADE A CHEESE BOARD!!!",
            "body" : """Hi! This is my first Cheese Board on the app, I used 
            Somerset-Brie, Gorgonzola and Edam, and paired it with grapes, cherry 
            tomatoes, selected nuts, prunes, digestives and a glass of peach ice tea.""",
            "likes" : 4, 
            "timeDate" : datetime.date(2021,03,05),
            "Account" : "Carlie19",
            "cheeses" : ["Somerset-Brie", "Gorgonzola", "Edam"],
        },
        {
            "ID" : 2,
            "title" : "Made another board!",
            "image" : "PostImages/cheese Board.jpg",
            "caption" : "I MADE ANOTHER CHEESE BOARD!!!",
            "body" : """Hi! This is my second Cheese Board on the app, I used 
            Camenbert, Cheddar and Edam, and paired it with grapes, apples
            , pecans, cranberry chutney and honey.""",
            "likes" : 2, 
            "timeDate" : datetime.date(2021,05,05),
            "Account" : "Carlie19",
            "cheeses" : ["Somerset-Brie", "Gorgonzola", "Edam"],
        },
        {
            "ID" : 3,
            "title" : "Cheese board trois!!!",
            "image" : "PostImages/images.jpg",
            "caption" : "Look at this presentation of confectionary delights",
            "body" : """On todays board we have a pork pate with mini cheddars, 
            cheddar, jarlsberg, mozzarella and red Leister, paired with fig,
            pickled onions, chilli and grapes.""",
            "likes" : 3, 
            "timeDate" : datetime.date(2023,09,05),
            "Account" : "Carlie19",
            "cheeses" : ["Cheddar", "Jarlsberg", "Mozzarella", "Red Leister"],
        },
        {
            "ID" : 4,
            "title" : "Hello CheeseBoard",
            "image" : "PostImages/BOARD.jpg",
            "caption" : "Questions about Somerset-Brie",
            "body" : """Was gifted a somerset brie over christmas and was wondering 
            what I can pair / eat it with, and also differenced between somerset brie 
            and it's french counterpart""",
            "likes" : 12, 
            "timeDate" : datetime.date(2024,01,01),
            "Account" : "Steve",
            "cheeses" : ["Somerset-Brie"],
        },
        {
            "ID" : 5,
            "title" : "Wake up honey, new cheese board dropped",
            "image" : "PostImages/How-to-Make-a-Cheese-Board-11.jpg",
            "caption" : "Little spring board",
            "body" : """Tight little cheese board with seed buiscuits, walnuts, 
            wensleydale, red leister and halloumi, with branston pickle, carrots, 
            apples, grapes and rosemary""",
            "likes" : 6, 
            "timeDate" : datetime.date(2024,03,03),
            "Account" : "Carlie19",
            "cheeses" : ["Wensleydale", "Red Leister", "Halloumi"]
            }
    ]
    
    saved = [
        {
            "name" : "Carl Posts",
            "posts" : [1,2,3,5],
            "account" : "Steve",
        }
    ]

    comment = [
        {
            "ID" : 1,
            "likes" : 1,
            "body" : "I like thif",
            "timeDate" : datetime.date(2024,04,03),
            "post" : 5,
            "account" : "Marge",
        },
        {
            "ID" : 2,
            "likes" : 3,
            "body" : "^s",
            "timeDate" : datetime.date(2024,04,03),
            "post" : 5,
            "account" : "Marge",
        },
        {
            "ID" : 3,
            "likes" : 3,
            "body" : "Looks lovely",
            "timeDate" : datetime.date(2024,05,03),
            "post" : 5,
            "account" : "Steve",
        },
        {
            "ID" : 1,
            "likes" : 7,
            "body" : "One is from somerset, the other isn't",
            "timeDate" : datetime.date(2024,04,03),
            "post" : 4,
            "account" : "Carlie19",
        },
    ]

    def add_cheese(_name):
        c=Cheese.objects.get_or_create(name = _name)[0]
        c.save()
        return c

    def add_stat(_ID,_time, _posts, _lT, _lG, _cT, _cG, _cR):
        s = Stats.objects.get_or_create(ID = _ID)[0]
        s.timeOnCheeseBoard = _time
        s.posts = _posts
        s.likesTaken = _lT 
        s.likesGiven = _lG
        s.commentsTaken = _cT 
        s.commentsGiven = _cG 
        s.cheesesReferenced = _cR
        s.save()
        return s
    
    def add_badge(_name):
        b = Badge.objects.get_or_create(name = _name)
        b.save()
        return b
    
    def add_account(_username, _password, _email, _forename, _surname,
                    _dOB, _accountCreationDate, _dateLastIn, _profile,
                    _stats, _faveCheese, _followers, _following, _badges):
        a = Account.objects.get_or_create(user = _username)
        a.user.username = _password
        
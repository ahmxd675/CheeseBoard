from datetime import datetime, timedelta
from django.shortcuts import render
from CheeseBoardSite.models import Account, Post, Cheese, Stats
from CheeseBoardSite.forms import UserForm, AccountForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
import random


def index(request):
    context_dict = {}
    
    
    #most_cheese_points_accounts_list = Account.objects.order_by('-cheese_points')[:10]
    
    context_dict['tags'] = tag_to_list(Cheese.objects.all())
    context_dict['posts'] = posts_to_list(Post.objects.all())

    # most_liked_posts_last_week_list = Post.objects.filter(timeDate__gte =(datetime.now() - timedelta(days=7))).order_by('-likes')[:10]
    #if request.user.is_authenticated:
    #   latest_posts_from_following_list = Post.objects.order_by('-timeDate')[:10]
    # context_dict['mostLiked'] += posts_to_list(most_liked_posts_last_week_list)
    # context_dict['followingPosts'] += posts_to_list(latest_posts_from_following_list)
    
    #context_dict['posts'] += posts_to_list(most_cheese_points_accounts_list)
    
    return render(request, 'CheeseBoardSite/index.html', context=context_dict)

def tag_to_list(tag_list):
    result_list =[]
    for tag in tag_list:
        result_list.append(tag.name)
    return result_list

def posts_to_list(post_list):
    result_list = []
    for post in post_list:
        result_list.append({
            "title": post.title,
            "content": post.body,
            "img": post.image,
            "slug": post.slug
        })
    return result_list
    

def register(request):
    registered = False

    if request.method == 'POST':
        #try get info
        user_form = UserForm(request.POST)
        account_form = AccountForm(request.POST)
    
        if user_form.is_valid() and account_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            account = account_form.save(commit=False)
            account.user = user
            account.accountCreationDate = timezone.now()
            account.dateLastLoggedIn = timezone.now()
            made = False
            while not made:
                s,m=Stats.objects.get_or_create(ID = random.randint(0,999999999))
                if m:
                    made = True
            s.save()
            account.stats = s
            # if 'profilePic' in request.FILES:
            #     account.profilePic = request.FILES['profilePic']
            
            account.save()
            registered = True
            return redirect("/")

        else:
            print(user_form.errors, account_form.errors)
    else:
        # not http post, use empty form for user input
        user_form = UserForm()
        account_form = AccountForm()

    return render(request, 'CheeseBoardSite/register.html',
                  context = {'user_form': user_form,
                             'account_form': account_form,
                             'registered': registered})
    

def account(request):
    if request.user.is_authenticated:
        userAccount = Account.objects.get(user = request.user)
        context_dict = {
            "username": request.user.username,
            "email": request.user.email,
            "forename": request.user.first_name,
            "surname": request.user.last_name,
            "dateOfBirth": userAccount.dateOfBirth,
            "accountCreationDate": userAccount.accountCreationDate,
            "dateLastLoggedIn": userAccount.dateLastLoggedIn,
            "profilePic": userAccount.profilePic,
            "stats": userAccount.stats,
            "faveCheese": userAccount.faveCheese,
            "followers": userAccount.followers.count(),
            "following": userAccount.following,
            "badges": userAccount.badges,
        }

        return render(request, 'CheeseBoardSite/account.html', context=context_dict)
    else:
        return redirect(reverse('CheeseBoardSite:login'))


def user_login(request):
    if request.method == 'POST':
        # try get info
        username = request.POST.get('username')
        password = request.POST.get('password')

        isValidLogin = authenticate(username=username, password=password)

        if isValidLogin:
            if isValidLogin.is_active:
                # if valid account is active log them back in
                login(request, isValidLogin)
                return redirect(reverse('CheeseBoardSite:index'))
            else:
                # account is inactive
                return HttpResponse("Account is disabled.")
        else:
            # not valid login details
            print(f"Login details are incorrect.")
            return HttpResponse("Incorrect Login details.")
    else:
        # not a http post
        return render(request, 'CheeseBoardSite/login.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.account = request.user.account  
            post.timeDate = timezone.now()  
            post.likes = 0  
            post.save()
        
            return redirect('/')  
    else:
        form = PostForm()
    #account = Account.objects.get(user = request.user)
    #account.cheese_points +=10
    #account.save() 
    return render(request, 'CheeseBoardSite/create_post.html', {'post_form': form})
    
@login_required
def user_logout(request):
    logout(request)

    # go back to homepage
    return redirect(reverse('CheeseBoardSite:index'))

def search(request, query):
    context_dict = {}
    posts = Post.objects.filter(
        Q(title__icontains=query) | 
        Q(body__icontains=query) |
        Q(cheeses__name__icontains=query)
    ).distinct()
    context_dict['posts'] = posts_to_list(posts)
    context_dict['tags'] = Cheese.objects.all()
    return render(request, 'CheeseBoardSite/search.html', context=context_dict)


def view_page(request):
    pass

def view_post(request, slug):
    if slug:
        post_slug = slug
        post = Post.objects.get(slug=post_slug)
        context_dict = {
            'title' : post.title,
            'image' : post.image,
            'caption' : post.caption,
            'body' : post.body,
            'likes' : post.likes,
            'timeDate' : post.timeDate,
            'account' : post.account,
            'cheeses': post.cheeses,
            'likes': post.likes,
            'cheeses': post.cheeses.all(),
        }
        return render(request, 'CheeseBoardSite/post.html', context = context_dict)
    

@login_required
def edit_page(request):
    pass

@login_required
def follow(request):
    pass

@login_required
def like_post(request):
    request.user.cheese_points +=1
    pass

@login_required
def comment_post(request):
    request.user.cheese_points +=5
    pass

@login_required
def save_post(request):
    pass

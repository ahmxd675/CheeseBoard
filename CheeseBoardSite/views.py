from datetime import datetime, timedelta
from django.shortcuts import render
from CheeseBoardSite.models import Account, Post, Cheese
from CheeseBoardSite.forms import UserForm, AccountForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone



def index(request):
    # Processing here for most popular tags, expected to be a list of strings 
    # TEMP DATA
    context_dict = {}
    # context_dict = {'tags':[
    #     "Cheddar",
    #     "Gouda",
    #     "Brie",
    #     "Swiss",
    #     "Mozzarella",
    #     "Provolone",
    #     "Blue",
    #     "Feta",
    #     "Havarti",
    #     "Gorgonzola",
    #     "Monterey Jack"
    # ],
    # # Processing here for most recent posts, expected to be a list of dictionaries
    # # TEMP DATA
    # 'posts': [
    #     {
    #         "title": "Post 1",
    #         "content": "This is the first post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 2",
    #         "content": "This is the second post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 3",
    #         "content": "This is the third post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 4",
    #         "content": "This is the fourth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 5",
    #         "content": "This is the fifth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 6",
    #         "content": "This is the sixth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 7",
    #         "content": "This is the seventh post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 8",
    #         "content": "This is the eighth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 9",
    #         "content": "This is the ninth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 10",
    #         "content": "This is the tenth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 11",
    #         "content": "This is the eleventh post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 12",
    #         "content": "This is the twelfth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 13",
    #         "content": "This is the thirteenth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 14",
    #         "content": "This is the fourteenth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 15",
    #         "content": "This is the fifteenth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    #     {
    #         "title": "Post 16",
    #         "content": "This is the sixteenth post.",
    #         "img": "\media\cheese.jpg"
    #     },
    # ]}
    
    #most_cheese_points_accounts_list = Account.objects.order_by('-cheese_points')[:10]
    
    #context_dict['tags'] = tag_to_list(Cheese.objects.all())
    context_dict['posts'] = posts_to_list(Post.objects.all())

    # most_liked_posts_last_week_list = Post.objects.filter(timeDate__gte =(datetime.now() - timedelta(days=7))).order_by('-likes')[:10]
    # latest_posts_from_following_list = Post.objects.order_by('-timeDate')[:10]
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
    result_list =[]
    for post in post_list:
        result_list += {
            "title": post.title,
            "content": post.content,
            "img": post.image
        }
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
            # if 'profilePic' in request.FILES:
            #     account.profilePic = request.FILES['profilePic']
            
            account.save()
            registered = True

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
def user_logout(request):
    logout(request)

    # go back to homepage
    return redirect(reverse('CheeseBoardSite:index'))

def search(request, query):
    context_dict = {'query': query}
    return render(request, 'CheeseBoardSite/search.html', context=context_dict)

def view_page(request):
    pass

def view_post(request):
    return render(request, 'CheeseBoardSite/post_card.html')

@login_required
def edit_page(request):
    pass

@login_required
def follow(request):
    pass

@login_required
def new_post(request):
    pass

@login_required
def like_post(request):
    pass

@login_required
def comment_post(request):
    pass

@login_required
def save_post(request):
    pass
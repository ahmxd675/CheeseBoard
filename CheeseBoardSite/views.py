from django.shortcuts import render
from CheeseBoardSite.forms import UserForm, AccountForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

def index(request):
    # Processing here for most popular tags, expected to be a list of strings 
    # TEMP DATA
    context_dict = {'tags':[
        "Cheddar",
        "Gouda",
        "Brie",
        "Swiss",
        "Mozzarella",
        "Provolone",
        "Blue",
        "Feta",
        "Havarti",
        "Gorgonzola",
        "Monterey Jack"
    ],
    # Processing here for most recent posts, expected to be a list of dictionaries
    # TEMP DATA
    'posts': [
        {
            "title": "Post 1",
            "content": "This is the first post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 2",
            "content": "This is the second post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 3",
            "content": "This is the third post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 4",
            "content": "This is the fourth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 5",
            "content": "This is the fifth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 6",
            "content": "This is the sixth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 7",
            "content": "This is the seventh post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 8",
            "content": "This is the eighth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 9",
            "content": "This is the ninth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 10",
            "content": "This is the tenth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 11",
            "content": "This is the eleventh post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 12",
            "content": "This is the twelfth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 13",
            "content": "This is the thirteenth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 14",
            "content": "This is the fourteenth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 15",
            "content": "This is the fifteenth post.",
            "img": "\media\cheese.jpg"
        },
        {
            "title": "Post 16",
            "content": "This is the sixteenth post.",
            "img": "\media\cheese.jpg"
        },
    ]}
    return render(request, 'CheeseBoardSite/index.html', context=context_dict)

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

            if 'profilePic' in request.FILES:
                account.profilePic = request.FILES['profilePic']
            
            account.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        # not http post, use empty form for user input
        user_form = UserForm()
        account_form = AccountForm()

    # need to check if this is the right link
    return render(request, 'CheeseBoard/register.html',
                  context = {'user_form': user_form,
                             'account_form': account_form,
                             'registered': registered})

def login(request):
    if request.method == POST:
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
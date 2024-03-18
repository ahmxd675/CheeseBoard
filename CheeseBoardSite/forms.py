from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from  CheeseBoardSite.models import Account, Cheese, Post

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class AccountForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput, required=False)
    dateOfBirth = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y'),
        label='Date of Birth'
    )
    
    class Meta:
        model = Account
        fields = ('dateOfBirth',)
        
        
class PostForm(forms.ModelForm):
    ID = forms.IntegerField()
    title =forms.CharField(max_length=64, help_text="Please enter the post title.")
    image = forms.ImageField(help_text="Please upload the image.")
    caption = forms.CharField(max_length=265, help_text="Please enter the caption.")
    body = forms.CharField(max_length=4096, help_text="Please enter the body of the post.")
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    timeDate = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    slug = forms.CharField(widget=forms.HiddenInput, required=False)
    #account = 
    #cheeses = 
    
    class Meta:
        model = Post
        exclude = ('account', 'cheeses')
        

class CheeseForm(forms.ModelForm):
    name = forms.CharField(max_length = 64, required=True)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)    
    
    class Meta:
        model = Cheese
        fields = ('name',)
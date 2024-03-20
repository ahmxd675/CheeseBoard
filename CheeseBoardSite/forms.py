from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from  CheeseBoardSite.models import Account, Cheese, Post

class UserForm(forms.ModelForm):
    passwordConfirm = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)
    field_order = ['username', 'email', 'password', 'passwordConfirm', 'first_name', 'last_name',]

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        passwordConfirm = cleaned_data.get('passwordConfirm')

        if password != passwordConfirm:
            raise forms.ValidationError("Passwords do not match.")
        
        for fieldName, fieldValue in cleaned_data.items():
            if fieldValue == "":
                raise forms.ValidationError("Please fill out " + fieldName)

class AccountForm(forms.ModelForm):
    dateOfBirth = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y'),
        label='Date of Birth'
    )
    faveCheese = forms.ModelChoiceField(queryset=Cheese.objects.all(), required=True, label="Favourite Cheese")
    
    class Meta:
        model = Account
        fields = ('dateOfBirth','faveCheese')
        
        
class PostForm(forms.ModelForm):
    title =forms.CharField(max_length=64, help_text="Please enter the post title.")
    image = forms.ImageField(help_text="Please upload the image.")
    caption = forms.CharField(max_length=265, help_text="Please enter the caption.")
    body = forms.CharField(max_length=4096, help_text="Please enter the body of the post.")
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    timeDate = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    slug = forms.CharField(widget=forms.HiddenInput, required=False)
    # account = 
    cheeses = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Cheese.objects.all(), required=False)
    
    class Meta:
        model = Post
        exclude = ('account', 'cheeses')
        

class CheeseForm(forms.ModelForm):
    name = forms.CharField(max_length = 64, required=True)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)    
    
    class Meta:
        model = Cheese
        fields = ('name',)
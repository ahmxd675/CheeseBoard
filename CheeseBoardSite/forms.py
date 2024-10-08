from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from  CheeseBoardSite.models import Account, Cheese, Comment, Post, Saved


class AccountSettingsForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput, required=True)
    email = forms.EmailField(widget = forms.TextInput, required=True)
    forename = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'forename', 'surname')
        
    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(AccountForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

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
    cheeses = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Cheese.objects.all(), required=False)
    
    class Meta:
        model = Post
        exclude = ('account',)
        

class CheeseForm(forms.ModelForm):
    name = forms.CharField(max_length = 64, required=True)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)    
    
    class Meta:
        model = Cheese
        fields = ('name',)
        
        
class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length= 250, required = True)
    class Meta:
        model = Comment
        fields = ['body', ]
        
class SavedForm(forms.ModelForm):
    name = forms.CharField(widget=forms.HiddenInput, max_length= 50, required = True)
    
    class Meta:
        model = Saved
        fields = ['name', 'posts', 'account']
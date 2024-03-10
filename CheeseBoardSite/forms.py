from django import forms
from django.contrib.auth.models import User
from  CheeseBoardSite.models import Account

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('dateOfBirth','accountCreationDate','dateLastLoggedIn','profilePic',)
from django import forms
from django.contrib.auth.models import User
from  CheeseBoardSite.models import Account

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class AccountForm(forms.ModelForm):
    dateOfBirth = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y'),
    )
    class Meta:
        model = Account
        fields = ('dateOfBirth','profilePic')
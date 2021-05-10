from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1','password2']
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class WorkingRegisterForm(ModelForm):
    class Meta:
        model = WorkingUser
        fields = ['mobile','image','gender']
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        r = WorkingUser.objects.filter(mobile=mobile)
        if r.count():
            raise  ValidationError("mobile number already exists")
        return mobile


class WorkingUpdateForm(ModelForm):
    class Meta:
        model = WorkingUser
        fields = ['mobile','image']
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        r = WorkingUser.objects.filter(mobile=mobile)
        if r.count()>1:
            raise  ValidationError("mobile number already exists")
        return mobile

class UserUpdateForm(ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count()>1:
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count()>1:
            raise  ValidationError("Email already exists")
        return email

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class UserForm(UserChangeForm):
    email = forms.EmailField(label="이메일")


    class Meta:
        model = User
        fields = ("username", "email")










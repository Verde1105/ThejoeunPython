from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


# class UserForm(UserChangeForm):#기본적으로 가진, 이름, 패스워드1패스워드2에 부가정보 이메일속성 추가
class UserForm(UserCreationForm):#기본적으로 가진, 이름, 패스워드1패스워드2에 부가정보 이메일속성 추가
    email = forms.EmailField(label="이메일")


    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        # fields = ("username", "email")





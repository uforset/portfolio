from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class SignupForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['username', 'password1', 'password2', 'nickname', 'university', 'location']
    labels = {
      'username': '이름입니다',
      'password1' : '비밀번호',
      'password2' : '비밀번호 확인',
      'nickname' : '닉네임 적어주세요',
      'university': '대학교 적어주세요',
      'location' : '거주 장소를 적어주세요',
    }
    widgets = {
      'username': forms.TextInput(attrs={'placeholder': "이름"}),
      'password1': forms.TextInput(attrs={'placeholder': "비밀번호"}),
      'password2': forms.TextInput(attrs={'placeholder': "비밀번호"}),
      'nickname': forms.TextInput(attrs={'placeholder': "닉네임을 적어주세요"}),
      'university': forms.TextInput(attrs={'placeholder': "대학교를 적어주세요"}),
      'location': forms.TextInput(attrs={'placeholder': "거주 장소를 적어주세요"}),
    }
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignupForm
from .models import CustomUser

# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return HttpResponse('로그인 성공')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# 구글링
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('/')
        return redirect('members:signup_view')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def log_out(request):
    if request.user.is_active:
        test = CustomUser.objects.get(is_active=True)
        test.is_active=False
        test.save()
        return redirect('/')

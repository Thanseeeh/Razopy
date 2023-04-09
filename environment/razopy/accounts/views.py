from django.shortcuts import render

# Create your views here.


def sign_up(request):
    return render(request, 'accounts_temp/sign-up.html')


def login_user(request):
    return render(request, 'accounts_temp/login.html')


def logout_user(request):
    return render(request, 'users_temp/index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages

# Create your views here.

def admin_home(request):
    return render(request, 'admins_temp/admin-home.html')


def admin_user_control(request):
    return render(request, 'admins_temp/admin-user.html')


def admin_wallet(request):
    return render(request, 'admins_temp/admin-wallet.html')


def admin_base(request):
    return render(request, 'admins_temp/admin-base.html')


def admin_logout(request):
    return render(request, 'admins_temp/admin-home.html')


#Admin login
def admin_login(request):
    if request.method == 'POST':
        email       = request.POST['email']
        password    = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None and user.is_superadmin:
            login(request, user)
            return redirect('admin_home')
        else:
            messages.info(request, 'Admin not Exist')
            return redirect('admin_login')
    else:
        return render(request, 'admins_temp/admin-login.html')
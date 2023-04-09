from django.shortcuts import render

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
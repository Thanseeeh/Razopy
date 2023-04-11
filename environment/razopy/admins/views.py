from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages
from django.db.models import Q
from django.apps import apps

Account = apps.get_model('accounts', 'Account')

# Create your views here.

def admin_home(request):
    return render(request, 'admins_temp/admin-home.html')



#User Controls
def admin_user_control(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Account.objects.filter(Q(username__icontains=q) | Q(email__icontains=q))
    else:
        data = Account.objects.all()

    context = {'data': data,}
    return render(request, 'admins_temp/admin-user.html', context)


def admin_wallet(request):
    return render(request, 'admins_temp/admin-wallet.html')


def admin_base(request):
    return render(request, 'admins_temp/admin-base.html')



#Admin logout
def admin_logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out')
    return redirect('admin_login')



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
    



#Block user
def block_user(request, user_id):
    user = Account.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect('admin_user_control')



#UnBlock user
def unblock_user(request, user_id):
    user = Account.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('admin_user_control')
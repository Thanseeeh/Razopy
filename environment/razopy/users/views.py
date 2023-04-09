from django.shortcuts import render

# Create your views here.


#Home
def home(request):
    return render(request, 'users_temp/index.html', {})


#Items
def items(request):
    return render(request, 'users_temp/items.html')


#Catogories
def categories(request):
    return render(request, 'users_temp/categories.html')


#Notice
def notice(request):
    return render(request, 'users_temp/notice.html')


#Profile
def profile(request):
    return render(request, 'users_temp/profile.html')


#Cart
def cart(request):
    return render(request, 'users_temp/cart.html')


#Create
def create(request):
    return render(request, 'users_temp/create.html')


#Base
def base(request):
    return render(request, 'users_temp/base.html')

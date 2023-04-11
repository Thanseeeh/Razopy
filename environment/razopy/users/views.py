from django.shortcuts import render, redirect
from .forms import TokenForm
from django.apps import apps
from .models import Token

Account = apps.get_model('accounts', 'Account')

# Create your views here.


#Home
def home(request):
    return render(request, 'users_temp/index.html', {})


#Items
def items(request):
    tokens = Token.objects.all()
    context = {'tokens': tokens}
    return render(request, 'users_temp/items.html', context)


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
    user_id = request.user.id
    user = Account.objects.get(id=user_id)
    if request.method == 'POST':
        form = TokenForm(request.POST, request.FILES)
        if form.is_valid():
            token = form.save(commit=False)
            token.owner = user
            token.save()
            return redirect('home')
    else:
        form = TokenForm()
    context = {'form': form, 'user': user, 'user_id': user_id}
    return render(request, 'users_temp/create.html', context)




#Base
def base(request):
    return render(request, 'users_temp/base.html')

from django.shortcuts import render, redirect
from .forms import TokenForm
from django.apps import apps
from .models import Token

Account = apps.get_model('accounts', 'Account')
Category = apps.get_model('admins', 'Category')
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
    if 'email' in request.session:
        return render(request, 'users_temp/profile.html')
    else:
        return redirect('/')


#Cart
def cart(request):
    if 'email' in request.session:
        return render(request, 'users_temp/cart.html')
    else:
        return redirect('login_user')
        


#Create
def create(request):
    if 'email' or 'super_email' in request.session:
        user_id = request.user.id
        user = Account.objects.get(id=user_id)
        data = Category.objects.all()
        if request.method == 'POST':
            form = TokenForm(request.POST, request.FILES)
            if form.is_valid():
                token = form.save(commit=False)
                token.owner = user
                token.save()
                return redirect('home')
        else:
            form = TokenForm()
        context = {'form': form, 'user': user, 'user_id': user_id, 'data': data}
    else:
        return redirect('home')
    return render(request, 'users_temp/create.html', context)




#Base
def base(request):
    return render(request, 'users_temp/base.html')

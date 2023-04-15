from django.shortcuts import render, redirect, get_object_or_404
from .forms import TokenForm
from django.apps import apps
from .models import *
from accounts.forms import Profileform
from django.contrib import messages
from django.conf import settings

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
        user = request.user
        tokens = Token.objects.filter(owner=user)
        total_token = tokens.count()
        context = {'tokens': tokens, 'total_token': total_token}
        return render(request, 'users_temp/profile.html', context)
    else:
        return redirect('/')



#Edit Profile
def edit_profile(request):
    user = request.user
    form = Profileform(instance=user)

    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Success!! Your profile has been updated successfully.')
            return redirect('edit_profile')
        else:
            print(form.errors)
            messages.error(request, 'There was an error updating your profile.')
    
    context = {'user': user, 'form': form}
    return render(request, 'users_temp/edit-profile.html', context)



#Remove profile
def remove_profile(request, user_id):
    account = Account.objects.get(id=user_id)
    account.profile_pic = settings.MEDIA_ROOT + '/profile.png'
    account.save()
    messages.success(request, 'Oops! your profile picture removed')
    return redirect(edit_profile)



#Cart
def cart(request):
    cart_owner = request.user
    cart = Cart.objects.filter(cart_owner=cart_owner, submitted=False).first()
    cart_items = CartItems.objects.filter(account=cart_owner).select_related('cart_items')
    items_count = cart_items.count()
    
    # total price
    if not cart_items.exists():
        total_price = 0
        if cart:
            cart.total_price = 0
            cart.save()
    else:
        total_price = cart.total_price if cart else 0
       
    context = {
        'cart_owner': cart_owner,
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
        'items_count': items_count,
    }
    return render(request,'users_temp/cart.html',context)




#Add to Cart
def addtocart(request, id):
    token = get_object_or_404(Token, id=id)
    user = request.user
    cart, created = Cart.objects.get_or_create(cart_owner=user, submitted=False)
    cart_item, created = CartItems.objects.get_or_create(cart_items=token, account=user)
    cart_item.save()
    cart.total_price += token.price
    cart.save()
    if created:
        messages.success(request, 'Added to cart successfully')
    return redirect('items')



#Remove item from cart
def remove_item(request, id):
    cart_owner = request.user
    cart = Cart.objects.filter(cart_owner=cart_owner, submitted=False).first()
    cart_item = CartItems.objects.get(id=id)
    if cart_item:
        cart.total_price -= cart_item.cart_items.price
        cart_item.delete()
        cart_items = CartItems.objects.filter(account=cart_owner)
        if not cart_items.exists():
            cart.total_price = 0
        cart.save()
    return redirect('cart')

        


#Checkout
def checkout(request):
    return render(request, 'users_temp/checkout.html')



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
                return redirect('items')
        else:
            form = TokenForm()
        context = {'form': form, 'user': user, 'user_id': user_id, 'data': data}
    else:
        return redirect('home')
    return render(request, 'users_temp/create.html', context)



#Base
def base(request):
    user = Account.objects.all()
    context = {'user': user}
    return render(request, 'users_temp/base.html', context)

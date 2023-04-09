from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('items/',views.items, name='items'),
    path('categories/',views.categories, name='categories'),
    path('notice/',views.notice, name='notice'),
    path('profile/',views.profile, name='profile'),
    path('cart/',views.cart, name='cart'),
    path('create/',views.create, name='create'),
    path('base/',views.base, name='base'),
]

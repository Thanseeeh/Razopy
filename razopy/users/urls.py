from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('items/',views.items, name='items'),
    path('categories/',views.categories, name='categories'),
    path('notice/',views.notice, name='notice'),
    path('profile/',views.profile, name='profile'),
    path('edit-profile/',views.edit_profile, name='edit_profile'),
    path('remove-profile/<int:user_id>',views.remove_profile, name='remove_profile'),
    path('cart/',views.cart, name='cart'),
    path('addtocart/<int:id>',views.addtocart, name='addtocart'),
    path('remove-item/<int:id>', views.remove_item, name="remove_item"),
    path('sell/<int:id>', views.sell, name='sell'),
    path('cancel-sale/<int:id>', views.cancel_sale, name='cancel_sale'),
    path('checkout/',views.checkout, name='checkout'),
    path('create/',views.create, name='create'),
    path('single-item/<int:id>', views.single_item, name='single_item'),
    path('base/',views.base, name='base'),
]

from django.urls import path, include
from . import views


urlpatterns = [
    path('admin-home/',views.admin_home, name='admin_home'),
    path('admin-user-control/', views.admin_user_control, name='admin_user_control'),
    path('admin-wallet/', views.admin_wallet, name='admin_wallet'),
    path('admin-base/',views.admin_base, name='admin_base'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('', views.admin_login, name='admin_login'),
    path('admin-home/block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('admin-home/unblock_user/<int:user_id>/', views.unblock_user, name='unblock_user'),
]
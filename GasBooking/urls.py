from django.contrib import admin
from django.urls import path
from gas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('admin_home',admin_home,name='admin_home'),
    path('booking',booking,name='booking'),
    path('user',user,name='user'),
    path('signup',signup,name='signup'),
    path('user_home',user_home,name='user_home'),
    path('Logout',Logout,name='Logout'),
    path('book_now',book_now,name='book_now'),
    path('my_booking',my_booking,name='my_booking'),
    path('delete_booking/<int:id>',delete_booking,name='delete_booking'),
    path('change_status/<int:id>',change_status,name='change_status'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    path('feedback',feedback,name='feedback'),
    path('view_feedback',view_feedback,name='view_feedback'),
    path('delete_feedback/<int:id>',delete_feedback,name='delete_feedback'),
    path('about',about,name='about'),
]

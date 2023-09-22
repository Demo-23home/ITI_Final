from django.urls import path

from .views import *


app_name = 'website'


urlpatterns = [
    path('',home,name='home'),
    # path('',login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
    path('record/<int:pk>',book_detail,name='book_detail'),
    path('delete/<int:pk>',delete_record,name='delete_record'),
    path('update/<int:pk>',update_record,name='update_record'),
    path('new/', add_record, name='add_record'),
]

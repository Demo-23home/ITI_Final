from django.urls import path

from .views import *
# 

app_name = 'website'

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
    path('record/<int:pk>',book_detail,name='book_detail'),
    path('std/<int:pk>',std_detail,name='std_detail'),
    path('delete/<int:pk>',delete_record,name='delete_record'),
    path('update/<int:pk>',update_record,name='update_record'),
    path('new/', add_record, name='add_record'),
    path('register_student',register_student,name='register_student'),
    # path('student_login',student_login,name='student_login'),
    path('std_dash/<int:pk>',stu_dash,name='std_dash'),

    path('student_login/', custom_login, name='student_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

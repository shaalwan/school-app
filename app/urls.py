from django.urls import path

from .views import *

urlpatterns = [
  path('student',registerStudent.as_view(),name='signupStudent'),
  path('admin',registerAdmin.as_view(),name='signupAdmin'),
  path('login',login.as_view(),name='Login'),
  path('userlist',Userlistview.as_view({'get':'list'}),name='userlist'),
  path('user/<str:pk>',userview.as_view(),name='user')
]

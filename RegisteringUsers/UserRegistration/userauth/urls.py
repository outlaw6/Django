from django.conf.urls import url
from userauth import views

#TEMPLATE TAG =
app_name = 'userauth'

urlpatterns = [ url('register/', views.register, name='register')]

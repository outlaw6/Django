from django.conf.urls import url
from django.urls import path
from Login import views

urlpatterns = [ path('', views.users, name='users') ]

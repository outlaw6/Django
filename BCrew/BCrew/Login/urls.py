from django.conf.urls import url
from Login import views

app_name = 'Login'

urlpatterns = [  url('', views.index, name='index')           ]

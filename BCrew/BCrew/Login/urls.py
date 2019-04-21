from django.conf.urls import url
from Login import views

app_name = 'Login'

urlpatterns = [  url('register/', views.register, name='register'),
                 url('ulogin/', views.ulogin, name='ulogin')    ]

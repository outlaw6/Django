

from django.url import path
from groups import views

app_name = 'groups'

url_patterns = [  path('', views.ListGroups.as_view(), name='all'),
                  path('new/', views.CreateGroup.as_view(), name='create'),
                  path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single')]

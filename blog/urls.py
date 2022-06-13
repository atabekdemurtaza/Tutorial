from unicodedata import name
from django.urls import path 
from blog.views import post_list 
from blog.views import post_detail
from blog.views import post_new 
from blog.views import post_edit

urlpatterns = [
    path('', post_list, name='post-list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
]
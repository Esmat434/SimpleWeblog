from django.urls import path
from .views import (
    post_list,post_detail,contact,about
)

urlpatterns = [
    path('',post_list,name='home'),
    path('post/<slug:slug>/',post_detail,name='post'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about')
]
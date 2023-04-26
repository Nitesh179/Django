from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('app',index,name='home'),
    path('',index2, name='home2')
]

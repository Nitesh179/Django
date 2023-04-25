from django.contrib import admin
from django.urls import path, include
from ABC import views

urlpatterns = [
    path('',views.index,name='home'),
    # path('account/',include('django.contrib.auth.urls')),
    path('abc',views.abc),
    # path('^$',views.index,name='home'),
    # path('signup',views.signup,name='signup'),
    # path('login',views.loginn, name="login"),
    # path('logout',views.logoutt, name="logout"),
    # path('account/<choice>',views.account,name='user'),

    path('app',views.indx, name='admin')
]

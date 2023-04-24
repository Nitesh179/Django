from django.contrib import admin
from django.urls import path
from home import views


urlpatterns=[
    path("",views.index,name='home'),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),

    # path('login',views.logn,name='login page'),
    path('user/',views.signup,name="userhome"),
    path('user/<choice>',views.user, name="useraction"),

    
]
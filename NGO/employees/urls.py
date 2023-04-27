 
from django.urls import path
from employees import views

urlpatterns = [
    path('',views.index,name="home"),
    path('user/<choice>',views.userchoice,name="user"),
    path('/form',views.detail_form,name="wizardform")
]

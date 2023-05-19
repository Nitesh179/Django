from drowsiness.views import *
from django.urls import path


urlpatterns = [
    path('<id>', index, name="home"),
    path('', livefe,  name="live_camera"),

    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

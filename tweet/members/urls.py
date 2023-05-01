from django.urls import path   
from members.views import SentimentAnalysis,abc

urlpatterns = [
    path('',abc(),name="home"),
]
 
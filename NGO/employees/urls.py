 
from django.urls import path
from employees import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="home"),
    path('user/<choice>',views.userchoice,name="user"),
    path('form/',views.detail_form,name="wizardform"),
    path('formsubmit',views.handlesubmit, name="handlesubmit"),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

 
from django.urls import path,include
from Xmen import views

urlpatterns = [
    # path('',views.index,name='home'),
    path('form/',views.studentinput,name='studentform'),
    path('',views.indx,name='carthome'),
    path('add/',views.addItem,name='cartadd'),
    path('display/',views.displayItem,name='cartadd'),


    path('contact/',views.contact,name='contact'),
    path('customer/',views.customer,name='customerDetail'),
    path('add/',views.ADD,name="addcustomer"),
    path('edit/',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name="delete"),
]

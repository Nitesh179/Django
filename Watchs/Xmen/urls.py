 
from django.urls import path,include
from Xmen import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contact/',views.contact,name='contact'),
    path('customer/',views.customer,name='customerDetail'),
    path('add/',views.ADD,name="addcustomer"),
    path('edit/',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name="delete"),
]

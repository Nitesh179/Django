from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from Xmen.models import Contact
from Xmen.models import Customer
from django.contrib import messages
from Xmen.forms import Stud_form, ItemAddForm

 

# Create your views here.

def index(req):
   
    return render(req,'index.html')

def contact(request):
   
    if request.method=="POST":
        name=request.POST.get('name')
        dob=request.POST.get('date')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        msg=request.POST.get('msg')

        contact1=Contact(name=name, email=email, dob=dob, contact=contact, msg=msg)
        contact1.save()
         
        messages.success(request, 'Form submission successful')

    return render(request,'contact.html')

def customer(request):
    
    cust_detail=Customer.objects.all().order_by('-id') 
    context={
            'customers':cust_detail
    }
    return render(request,'customer.html',context)

def ADD(request):
    
   if request.method=="POST":
        
        name= request.POST.get('name')
        email= request.POST.get('email')
        address= request.POST.get('address')
        phone= request.POST.get('phone')

        cust=Customer(name=name, email=email, address=address, phone=phone)
        cust.save()
        
        return redirect('customerDetail')

   cust_detail=Customer.objects.all()
   context={
    'customers':cust_detail
    }
    # messages.success(request, "Successfully saved data!!!")
   
   
   return render(request,'customer.html',context)

def edit(request):
    cust_detail=Customer.objects.all()
    context={
            'customers':cust_detail
    }
    return render(request,'customer.html',context)
     
def update(request,id):
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        address= request.POST.get('address')
        phone= request.POST.get('phone')

        cust=Customer(id=id, name=name, email=email, address=address, phone=phone)
        cust.save()

    return redirect('customerDetail')

def delete(request,id):
    customer=Customer.objects.filter(id=id)
    customer.delete()
    return redirect('customerDetail')
    # return redirect(request,'customer.html',{'customers':customer})

def studentinput(request):
    send=False
    # forme=forms.Stud_form()
    if request.method=='POST':
        form=Stud_form(request.POST)
        if form.is_valid():
            print("Form is validate....")
            send=True
    forme=Stud_form()    
    return render(request,"index1.html",{'form':forme,'send':send})


def indx(request):
    return render(request,"home.html") 


# store data in cookie :
'''def addItem(request):
    form=ItemAddForm()
    res=render(request,'addItem.html',{'forms':form})
    if request.method == 'POST':
        form=ItemAddForm(request.POST)
        if form.is_valid():
           name =form.cleaned_data['itemName']
           qty =form.cleaned_data['itemQty']
           res.set_cookie(name,qty,180)
    return res'''

# store data in Session :
def addItem(request):
    form=ItemAddForm()
   
    if request.method == 'POST':
       name=request.POST['itemName']
       qty=request.POST['itemQty']
       request.session[name]=qty
    return render(request,'addItem.html',{'forms':form})    
         

def displayItem(request):
    return render(request,'showitem.html')
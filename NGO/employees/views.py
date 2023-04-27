from django.shortcuts import render,HttpResponse, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

# Create your views here.
def index(request):
    return render(request,"login/signup.html",{'signup':True})

@login_required(login_url='/') 
def detail_form(request):
    return render(request,"form/index.html")

def signin(request):
    if request.method=='POST':
        luser=request.POST['loginuser']
        lpass=request.POST['lpass']
        user=authenticate(username=luser, password=lpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully....")
            return redirect('wizardform')
        
        else:
            messages.success(request, "Wrong Credientials please try again.")
            return redirect('/user/login')
        
    else:
        return render(request, "login/signup.html",{'signup':False})
        
def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)<2:
            messages.error(request, "username should be more than 2 character...")
            return redirect('wizardform')
        
        if pass1!=pass2:
            messages.error(request, "password does not match ") 
            return redirect('home')
        
        
        newuser=User.objects.create_user(username, email, pass1)
        newuser.save()

    else:
        messages.warning(request, "signup required ")
        return render('/')
    
@login_required(login_url='/user/login') 
def signout(request):
    logout(request)
    messages.success(request, "succesfully signout ") 




def userchoice(request,choice):
    if choice=='login':
        return signin(request)
    elif choice=='signup':
       return signup(request)
    elif choice=='logout':
        return signout(request)
     
     
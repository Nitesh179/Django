from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 


def abc(request):
    return HttpResponse("<h2> Hello django....</h2>")







# Create your views here.
@login_required(login_url='/login')
def indx(request):
   
    return render(request, "bank/index.html")

def index(request):
    # messages.success(request, "Login Succesfull")
    return render(request,"login/signup.html",{'signup':True})

# @login_required 
def signup(request):
    
    if request.method == "POST": 
        username = request.POST['username']
        email    = request.POST['email']
        pass1    = request.POST['pass1']
        pass2    = request.POST['pass2']

        if len(username)<2:
            messages.error(request,"name should be 2 or more letters ")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request,"passwords not match ")
            return redirect('home')


        newuser=User.objects.create_user(username, email, pass1)
        newuser.save()
        messages.success(request,"Your Account Created!!!")
        return redirect('home')
   
    # if newuser.is_authenticated:
       
    #   return render(request, "error.html", {'title':'Not allowed here', 'mess':'Signup first!!!'})
    
    else :
        return render(request, "error.html", {'title':'Multiple siggned In Not allow', 'mess':'You Already Logged In dont need to signup again.'})
        # return render(request, "login/signup.html", {'signup':True})
   
# @login_required(login_url='/')
def loginn(request):
    if request.method=='POST':
        loginuser=request.POST['loginuser']
        loginpass=request.POST['loginpass']
        user = authenticate(username=loginuser, password=loginpass)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Succesfully Logged In...")
            return redirect('admin')
        
        else:
            messages.error(request, "Invalid Credentials, Please try again...")
            return redirect('login')

    else :
        return render(request, "login/signup.html", {'signup':False})
       

def logoutt(request):
    logout(request)
    messages.info(request, "Logged Out Succesfully...")
    return redirect('home')
    

def account(request, choice):
    if choice == 'login':
        return loginn(request)
    
    elif choice == 'signup':
        return signup(request)
    
    elif choice == 'logout':
        return logoutt(request)
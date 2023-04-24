from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"this is kuch bhi message"
    }
    # return HttpResponse("this is home page....")
    return render(request,"index.html",context)

def about(request):
    # return HttpResponse("This is about page")
    return render(request,"about.html")


def contact(request):
    # return HttpResponse("This is contact page")
    return render(request,"contact.html")

@login_required(login_url="/user")
def logn(request):
    lemail=request.POST['loginemail']
    lpass=request.POST['loginpass']

    user=authenticate(username=lemail, password=lpass)
    print("==> ",user)
    if user is not None:
        login(request, user)
        messages.success(request, "user login succesfully....")
        return redirect('home')
    else:
        messages.error(request, "invalid user...")
        return redirect('home')
    

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass']

        newuser=User.objects.create_user(username, email, password)
        newuser.save()
        messages.success(request, "user succesfully register....")
        return redirect('home')  
        
    else : 
        messages.success(request, "some error found try agian....")
        return HttpResponse('<h3>NOT FOUND</h3>')


 
def user(request, choice):
    
    if choice == 'login':
        return logn(request)
    
    elif choice == 'signup':
       return signup(request)
    else : 
        return HttpResponse("<h2> Specific path not match</h2>")
    

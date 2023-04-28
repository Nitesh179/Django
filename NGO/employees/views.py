from django.shortcuts import render,HttpResponse, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from employees.models import Employee

# Create your views here.
def index(request):
    return render(request,"login/signup.html",{'signup':True})

@login_required(login_url='/') 
def detail_form(request):
    return render(request,"form/index.html")

def signin(request):
    if request.method=='POST':
        loginuser=request.POST['loginuser']
        loginpass=request.POST['loginpass']
        
        user=authenticate(username=loginuser, password=loginpass)
        print(user)

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
            return redirect('home')
        
        if pass1!=pass2:
            messages.error(request, "password does not match ") 
            return redirect('home')
        
        
        newuser=User.objects.create_user(username, email, pass1)
        newuser.save()
        return redirect('wizardform')
        

    else:
        messages.warning(request, "signup required ")
        return redirect('home')
    
@login_required(login_url='/user/login') 
def signout(request):
    logout(request)
    messages.success(request, "succesfully signout ") 
    return redirect('home')

 
def userchoice(request,choice):
    if choice=='login':
        return signin(request)
    elif choice=='signup':
       return signup(request)
    elif choice=='logout':
        return signout(request)
    
    # return HttpResponse("hello")
     

def handlesubmit(request):
    if request.method == "POST":
        pic = request.FILES['propic']
        print("==> ",pic)
        name = request.POST['name']
        dob = request.POST['dob']
        contact = request.POST['contact']
        email = request.POST['email']
        maritialstatus = request.POST['maritialstatus']
        gender = request.POST['gender']

        state = request.POST['state']
        city = request.POST['city']
        zip = request.POST['zip']

        address = request.POST['address']
        bankname = request.POST['bankname']
        accountno = request.POST['accountno']
        branch = request.POST['branch']
        ifsc = request.POST['ifsc']
        
        feedback = request.POST['feedback']

        emp = Employee(propic=pic, name=name, dob=dob, contact=contact, email=email, maritialstatus=maritialstatus, gender=gender,  state=state, city=city, zip=zip, address=address, bankname=bankname, accountno=accountno,branch=branch, ifsc=ifsc, feedback=feedback )
        emp.save()

        messages.success(request, "Your Detail Successfully Saved!!!!")
        return redirect('home')

    else:
        messages.error(request, "Something went wrong!!! Try Again")
        return redirect('wizardform')
    

        
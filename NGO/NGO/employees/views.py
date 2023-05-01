from django.shortcuts import render,HttpResponse, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from employees.models import Employee
# from employees.form import ImageForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.http import JsonResponse
from urllib.parse import parse_qs
import json

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
        return redirect('/user/login')

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
     
@csrf_exempt
def handlesubmit(request):
      if request.method=='POST':
          data=parse_qs(json.loads(request.body.decode('utf-8')))
          breakpoint()
          emp= Employee.objects.create( name=data['name'], dob=data['dob'], contact=data['contact'], email=data['email'], maritialstatus=data['maritialstatus'], gender=data['gender'],  state=data['state'], city=data['city'], zip=data['zip'], address=data['address'], bankname=data['bankname'], accountno=data['accountno'],branch=data['branch'], ifsc=data['ifsc'], feedback=data['feedback'] )
          emp.propic=data['propic']
        #   emp.save()
          messages.success(request, "Your Detail Successfully Saved!!!!")
          return HttpResponse("done")
      else:
       return HttpResponse("helo")
  
    
def detail(request):
    pass
    
        
 

















   #     # name = request.POST.get('name'),
    #     # dob = request.POST.get('dob'),
    #     # contact = request.POST.get('contact')
    #     # email = request.POST.get('email')
    #     # maritialstatus = request.POST.get('maritialstatus')
    #     # gender = request.POST.get('gender')

    #     # state = request.POST.get('state')
    #     # city = request.POST.get('city')
    #     # zip = request.POST.get('zip')

    #     # address = request.POST.get('address')
    #     # bankname = request.POST.get('bankname')
    #     # accountno = request.POST.get('accountno')
    #     # branch = request.POST.get('branch')
    #     # ifsc = request.POST.get('ifsc')
        
    #     # feedback = request.POST.get('feedback')

        

    #     # emp = Employee.objects.create( name=name, dob=dob, contact=contact, email=email, maritialstatus=maritialstatus, gender=gender,  state=state, city=city, zip=zip, address=address, bankname=bankname, accountno=accountno,branch=branch, ifsc=ifsc, feedback=feedback )
       
    #     # if len(request.FILES) == 0:
    #     #  print('no files')
    #     # else: 
    #     #   _, file = request.FILES.popitem()
    #     #   file = file[0]
    #     # #   print("==> ", file)
    #     # emp.propic = file
    #     # emp.save()
    #     # # pic = request.FILES.get("propic")
       
    #     # messages.success(request, "Your Detail Successfully Saved!!!!")
    #     # data = Employee.objects.all().values().last()
     
    #     # dataa=data.keys()
       
    #     return render(request, "form/index.html",{"data":data,"keys":dataa}, RequestContext(request))

    #  else:
    #     messages.error(request, "Something went wrong!!! Try Again")
    #     return redirect('wizardform')
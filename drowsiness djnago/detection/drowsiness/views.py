from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
import cv2
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from drowsiness.camera import *

# Create your views here.
def  index(request, id="h"):
    if id == "show":
        cap=cv2.VideoCapture(0)
        while True:
            ret, frames= cap.read()
            if ret:
                cv2.imshow("video",frames)
            if cv2.waitKey(1)==27:
                break
        cv2.destroyAllWindows()
        return render(request,'index.html')
    
    # else:
    return render(request, "signup.html")        
    


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')






@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:   
        pass
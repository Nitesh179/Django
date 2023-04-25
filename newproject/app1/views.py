from django.shortcuts import HttpResponse

def index(req):
    return HttpResponse("hello django")
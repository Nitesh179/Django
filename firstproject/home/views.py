from django.shortcuts import render, HttpResponse

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


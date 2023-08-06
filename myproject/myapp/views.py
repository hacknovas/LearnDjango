from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Mahi is good")

def index(request):
    context={
        "Name":"Doni"
    }
    return render(request,template_name="index.html",context=context)

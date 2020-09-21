from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        prof = Professor.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)
        print(prof)
        if prof[1]==True:
            return HttpResponse("<h1>Created Succesfully</h1>")
        else:
            return HttpResponse("<h1>Proffessor already present in database</h1>")
    return render(request, "index.html")

def pro_list(request):
    a = Professor.objects.all()
    print(a)
    return render(request,"pro_list.html", context={'a':a})

def update_data(request):
    if request.method=="POST":
        id = request.POST["id"]
        updata = request.POST["updata"]

        a = Subject.objects.filter(id=id).update(subject=updata)
    return render(request, "update.html")


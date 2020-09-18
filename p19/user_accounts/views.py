from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponse


def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            first_name= form.cleaned_data["first_name"]
            last_name= form.cleaned_data["last_name"]
            email= form.cleaned_data["email"]
            password= form.cleaned_data["password"]
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return HttpResponse("<h1>Thank you for the registration</h1>")
    form = UserForm
    return render(request, "signup.html",{"form":form})
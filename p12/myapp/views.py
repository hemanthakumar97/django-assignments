from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        job = request.POST['job']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        send_mail("Thank you for Registering", "Hello, {}.\nThank you for registering".format(name),"hktechlabs@gmail.com", 
        [email,], fail_silently=True)
        return HttpResponse("<h1>Name: {}</h1><h1>Email: {}</h1><h1>Phone Number: {}</h1><h1>Job: {}</h1>".format(name,email,phno,job))
    return render(request, 'register.html')
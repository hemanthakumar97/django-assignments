from django.shortcuts import render


def index(request):
    return render(request, "index.html",{"a":10,"b":30, "name":"hemanth"})

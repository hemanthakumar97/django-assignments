from django.shortcuts import render
from django.http import HttpResponse


def get_method(request):
    name=request.GET.get('name')
    return render(request, 'get_method.html', {'name':name})

def post_method(request):
    if request.method == "POST":
        name = request.POST['name']
        return HttpResponse("<h1>Thanks for the submition, {}".format(name))
    return render(request, 'post_method.html')

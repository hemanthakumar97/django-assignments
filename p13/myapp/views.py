from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def multiselect(request):
    if request.method=="POST":
        language = request.POST.getlist("language")
        return HttpResponse("<h1>{}</h1>".format(language))
    return render(request, "multiselect.html")
    
def img_upload(request):
    if request.method=="POST" and request.FILES:
        print("a")
        image = request.FILES['a']
        fs=FileSystemStorage()
        print(fs)
        print(image)
        fs.save(image.name, image)
    return render(request, "img_upload.html")

from django.shortcuts import render
from .forms import BuiltinForm

def builtinform(request):
    if request.method=="POST":
        form=BuiltinForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            return render(request, 'details.html', context=data)
    form = BuiltinForm()
    return render(request,"builtinfrom.html",{"form":form})

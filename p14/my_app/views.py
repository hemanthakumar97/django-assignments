from django.shortcuts import render
from .forms import BuiltinForm

def builtinform(request):
    form = BuiltinForm()
    return render(request,"builtinfrom.html",{"form":form})

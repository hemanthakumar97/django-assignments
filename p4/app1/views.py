from django.shortcuts import render

# Create your views here.

def add_n(request, nums):
    num = nums.split(" ")
    total = 0
    for i in range(len(num)):
        total = int(total) + int(num[i])
    return render(request, 'app1/add_n.html', {"total":total})



from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greatest(request,nums):
    num = nums.split(" ")
    if int(num[0]) > int(num[1]):
        greatest = num[0]
    elif int(num[1])> int(num[0]):
        greatest = num[1]
    else:
        greatest = "both are equal"

    context = { "greatest": greatest, }
    return render(request, 'url_data.html', context)

def greatest_of_n(request,nums):
    num = nums.split(" ")
    greatest = int(num[0])
    for i in range(len(num)):
        for j in range(1, len(num)):
            if int(num[j]) >= greatest:
                greatest = int(num[j])
    context = { "greatest": greatest, }
    return render(request, 'url_data.html', context)
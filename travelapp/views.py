from django.http import HttpResponse
from django.shortcuts import render

from .models import place, newspost


def fun(request):
    obj=place.objects.all()
    abc=newspost.objects.all()
    return render(request, 'index.html',{'results':obj,'values':abc})


def addition(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    num3 = num1 + num2
    return render(request, "result.html", {'add': num3})


# def abcd(request):
#     obj=newspost.objects.all()
#     return render(request,'index.html',{'values':obj})
# from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team
# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
# def about(request):
#     return render(request,'about.html')
# def addition(request):
#     n1=int(request.GET['num1'])
#     n2=int(request.GET['num2'])
#     result=n1+n2
#     return render(request,'add.html',{'res':result})

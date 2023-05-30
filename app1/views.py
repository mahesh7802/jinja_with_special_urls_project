from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def function(request):
    return HttpResponse('<h1>this is function in multiapplications</h1>')
d={'name':'RAJESH','money':2000,}
def money(request):
    return render(request,'money.html',context=d)
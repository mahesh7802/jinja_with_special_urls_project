from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def parents(request):
    return HttpResponse('<h1> CHADUVUKONDI RA MACHINGA UNTARU ')
d={'name':'jinja','year':1991}
def jinjaindex(request):
    return render(request,'jinjaindex.html',context=d)
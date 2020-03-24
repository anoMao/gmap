from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html",locals())

def test(request):
    return render(request,"test.html",locals())
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{'section':'index'})

def about(request):
    return render(request,'about.html',{'section':'about'})

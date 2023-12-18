from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'events.html')


def login(request):
      return render(request, 'trainers.html')


def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        user=User.objects.create_user(username=username,password=password)
        user.save();
#
        return render(request, 'trainers.html')
    else:

     return render(request,'register.html')

def detail(request):
    return render(request,'detail.html')
def form(request):
    return render(request,'form.html')
def newpage(request):
    return render(request,'newpage.html')
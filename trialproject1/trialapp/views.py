from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import place,team

# Create your views here.
def demo(request):
    obj=place.objects.all()
    mem=team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':mem})

def login(request):
     if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']
         user=auth.authenticate(username=username,password=password)

         if user is not None:
             auth.login(request,user)
             return redirect('/')
         else:
             messages.info(request,"Invalid entry")
             return redirect('login')
     return render(request,"login.html")

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)

            user.save();
            return redirect('login')

        else:
           messages.info(request,"Incorrect Password")
           return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')





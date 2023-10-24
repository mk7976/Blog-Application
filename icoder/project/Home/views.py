from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
#from django.contrib.messages import constants as messages
from .models import Contact_Us


# Create your views here.

def Home(request):
    return render(request, 'home.html')


def Contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if (len(name) < 3 or len(email) < 3) or (len(phone) < 10 or len(content) < 3):
            messages = "Please fill the form correctly"
            dict = {"messages": messages, "A": "danger"}
            return render(request, 'contact.html', {"messages": dict})

        else:
            messages = "Your Form is submitted."
            dict = {"messages": messages, "A": "success"}
            contact = Contact_Us(name=name, email=email, phone=phone, content=content)
            contact.save()
            print(11)
            return render(request, 'contact.html', {"messages": dict})
            # return redirect('contact/')
    return render(request, 'contact.html')


def About(request):
    return render(request, 'about.html')


def Signof(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        checkuser = User.objects.filter(email=email)
        checkusername = User.objects.filter(username=username)
        if len(checkuser) == 0 and len(checkusername) == 0:
            if pass2 == pass1:
                creatinguser = User.objects.create_user(username=username, email=email, password=pass1)
                messages = "Your iCoder has been successfully created."
                messages = {"messages": messages, "A": "success"}
                return render(request, "home.html", {"messages": messages})
            #return redirect('home')


        else:
            message = "You have already registered."
            messages = {"messages": message, "A": "warning"}
            return render(request, "home.html", {"messages": messages})


def login(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['loginusername']
        password = request.POST['pass']
        user = authenticate(request,username=username, password=password)
        #if checkuser.is_authenticated:
             #print(checkuser)
        if user is not None:
            auth_login(request,user)
            #messages.error(request, "Successfully Logged In")
            message = "You have logged in."
            messages = {"messages": message, "A": "success"}
            return render(request, "home.html", {"messages": messages, "user": user})
            #messages.success(request,"sd")
            #print(messages)
            return redirect('home')

        else:
            message = "You are not registred till now,please registered first."
            messages = {"messages": message, "A": "danger"}
            return render(request, "home.html", {"messages": messages})
            return redirect("/")



def logout(request):
    auth_logout(request)
    message = "You are logged out."
    messages = {"messages": message, "A": "success"}
    return render(request, "home.html", {"messages": messages})
    return redirect("/")


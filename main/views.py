

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

def HomePage(request,template_name="homepage.html"):

    if request.method =="POST":
        try:
            User.objects.create(
                                username=request.POST.get('fname')+" " + request.POST.get('lname'),
                                first_name=request.POST.get('fname'),
                                last_name=request.POST.get('lname'),
                                email=request.POST.get('email'),
                                password=request.POST.get('password')
            )
            messages.success(request,"User created  successfully ",fail_silently=True)
        except Exception as e :
            print("Error creating")
            pass

    return render(request, template_name,locals())
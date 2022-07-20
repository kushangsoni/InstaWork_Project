from multiprocessing import context
from pickle import TRUE
from tkinter.tix import Form
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from phonenumber_field.modelfields import PhoneNumberField


from django.views.generic import (ListView)


def home(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'InstaWork_App/home.html', context)

def edit(response,id):
    context = {
        'user': User.objects.get(id=id)
    }
    if response.method == "POST":
        if response.POST.get("save"):
            user = User.objects.get(id=id)
            
            user.firstName = response.POST['firstName']
            user.lastName = response.POST['lastName']
            user.emailID = response.POST['emailID']
            user.phoneNo = response.POST['phoneNo']

            user.save()

        elif response.POST.get("delete"):
            User.objects.get(id=id).delete()
         
        return render(response,'InstaWork_App/home.html', {'users': User.objects.all()})

    return render(response,'InstaWork_App/edit.html', context)
    

class UserListView(ListView):
    model= User
    template_name= 'InstaWork_App/home.html'
    context_object_name= 'users'


def add(request):
    if request.method == 'POST':
        if request.POST.get("save"):
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            emailID = request.POST['emailID']
            phoneNo = request.POST['phoneNo']
            

            if User.objects.create(firstName=firstName,lastName=lastName,emailID=emailID,phoneNo=phoneNo):
                return render(request,'InstaWork_App/home.html', {'users': User.objects.all()})
            else:
                return render(request,'InstaWork_App/add.html')        
            
    
    return render(request,'InstaWork_App/add.html')


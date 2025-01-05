from django.shortcuts import render
from django.http import HttpResponse
from .models import register
import hashlib
import json
from django.contrib import messages

# Create your views here.

def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        # confirmPassword = confirmPassword.encode()
        # confirmPassword = hashlib.sha256(confirmPassword)

        if password != confirmPassword:
            messages.error(request, "Passwords do not match!")
            # print(f"password: {password}/n")
            
            return render(request, "registration.html")
        # def read():
        #     # Open and read the JSON file
        #     with open('/workspaces/temp/ecom/registration/user.json', 'r') as file:
        #         data = json.load(file)
        #         for i in data:
        #             print(i)
        #             name = i['username']
        #             email = i['email']
        #             password = i['password']
        #             password = password.encode()
        #             password = hashlib.sha256(password)                
        #             reg = register(name = name, email = email, password = password)
        #             reg.save()    #saved to database
        #     return data
        # # print(read())
        # read()
        password = password.encode()
        password = hashlib.sha256(password)
        reg = register(name = name, email = email, password = password)
        # reg.save()    #saved to database
        print("-------------REGISTERED-------------")
        return HttpResponse("Registered succesfully!!")
    return render(request, "registration.html")

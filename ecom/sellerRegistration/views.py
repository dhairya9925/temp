from django.shortcuts import render
import json
import hashlib
from .models import countryCodes
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# from .insert import insert as ins
# Create your views here.

temp = {
    "name":"",
    "phone":"",
    "email":"",
    "password":""
}

def sellerRegistration(request):
    data = countryCodes.objects.all().values()
    first = data[0]
    if request.method == "POST":
        temp["name"] = request.POST["name"]
        temp["email"] = request.POST["email"]
        temp["phone"] = request.POST["phone"]
        password = request.POST["password"]
        password = password.encode()
        password = hashlib.sha256(password)
        temp["password"] = request.POST["password"]
        # country = countryCodes[1]
        print("-- REQUESTED \"POST\" METHOD --")
        # def insert():

        #     with open('/workspaces/temp/ecom/sellerRegistration/countryCode.json', "r+") as file:
        #         data = json.load(file)
        #         for val in data:
        #             country = val["name"]
        #             dialCodes = val["dialCodes"]
        #             image = val["image"]
        #             if len(dialCodes) > 1:
        #                 for dialCode in dialCodes:
        #                     sReg = countryCodes(country = country, dialCode = dialCode,image = image)
        #                     sReg.save()
        #                     print(f"country = {country}, dialCode = {dialCode},image = {image}")
        #                 print("--- More than 1 dialCode ---")
        #             else:
        #                 sReg = countryCodes(country = country, dialCode = dialCodes[0],image = image)
        #                 sReg.save()
        #                 print(f"country = {country},\ndialCode = {dialCodes[0]},\nimage = {image}\n\n")
        #     return 0
        # print(country)
    else:
        print("-- REQUESTED \"GET\" METHOD --")
    return render(request, "sellerRegistration.html", {"data" : data, "first" : first} )

@csrf_exempt
def company(request):
    if request.method == 'POST':
        key = "8319d4c265cf5153ed247f0a05a0fd46"
        # gstInfo = f"https://sheet.gstincheck.co.in/check/{key}/{gstNumber}"
        # name = temp[0]
        # name = temp[0]
        # name = temp[0]
        # name = temp[0]
        for x in temp:
            print(x)
        print (f" --- Method \"POST\" --- ")
        return render(request, "company.html")
    print (f" --- Method \"GET\" --- ")
    return render(request, "company.html")
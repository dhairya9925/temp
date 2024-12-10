from django.shortcuts import render

# Create your views here.
def addproduct(request):
    return render(request, "addproduct.html")
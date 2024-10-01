from django.shortcuts import render

# Create your views here.
def sellerRegistration(request):
    return render(request, "sellerRegistration.html")
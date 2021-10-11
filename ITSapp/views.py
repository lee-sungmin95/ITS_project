from django.shortcuts import render

# Create your views here.

def ITS(request):
    return render(request, 'ITSapp/itsapp.html')
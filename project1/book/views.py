from django.shortcuts import render

# Create your views here.

def say_by(request):
    return render(request,'by.html')
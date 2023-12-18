from django.shortcuts import render

def home():
    return render(request,'usuarios/home.html')

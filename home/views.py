from django.shortcuts import render

def index(request):
    return render(request,'home/index.html')

def resume(request):
    return render(request,'home/resume.html')

def project(request):
    return render(request,'home/projet.html')

def contacts(request):
    return render(request,'home/contacts.html')
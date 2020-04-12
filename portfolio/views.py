from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()# to grab out the objects of the database
    return render(request,'home.html',{'projects':projects})

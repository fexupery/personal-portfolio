from django.contrib import admin
from .models import Project

#this line register the project in the admin console of django
admin.site.register(Project)

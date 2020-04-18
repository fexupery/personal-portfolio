from django.db import models

class Project(models.Model):
    #https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # to show in the admin console the object from database with the title instead of object 1, object 2, ...
    def __str__(self):
        return self.title

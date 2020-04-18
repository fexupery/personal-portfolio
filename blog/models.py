from django.db import models
from django.db.models import fields

class Blog(models.Model):
    title = fields.CharField(max_length=100)
    date = fields.DateField()
    content = fields.TextField(default='no content for this entry')

# to show in the admin console the object from database with the title instead of object 1, object 2, ...
    def __str__(self):
        return self.title

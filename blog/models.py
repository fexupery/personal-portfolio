from django.db import models
from django.db.models import fields

class Blog(models.Model):
    title = fields.CharField(max_length=100)
    date = fields.DateField()
    content = fields.TextField(default='no content for this entry')

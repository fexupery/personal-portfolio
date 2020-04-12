from django.db import models
from django.db.models import fields

class Blog(models.Model):
    title = fields.CharField(max_length=100)
    date = fields.DateField(auto_now_add=True)
    content = fields.CharField(max_length=5000, default='no content for this entry')

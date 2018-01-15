from django.db import models

# Create your models here.
class Editor(models.Model):
    """Class that create Editors objects"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    

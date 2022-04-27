from cgitb import html
from django.db import models

# Create your models here.
class webSite(models.Model):
    htmlString = models.TextField()
    companyName = models.CharField(max_length=60,default='No name')
    images = models.ImageField(upload_to='images/')
    

  

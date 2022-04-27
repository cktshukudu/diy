from cgitb import html
from django.db import models

# Create your models here.
class webSite(models.Model):
    htmlString = models.TextField()
    companyName = models.CharField(max_length=60,default='No name')
    images = models.ImageField(upload_to='images/')
    
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
  

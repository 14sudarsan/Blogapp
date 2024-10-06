from typing import Iterable
from django.db import models

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        
        return self.name


class Post(models.Model):
    
    title = models.CharField(max_length=10000)
    
    content = models.TextField()
    
    img_url = models.URLField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
   
    
    def __str__(self) -> str:
        return self.title
    
class AboutUs(models.Model):
    
    content = models.TextField()
    


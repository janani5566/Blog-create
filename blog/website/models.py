from django.db import models
from django.forms import SlugField

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(max_length=5000,blank=True,null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title
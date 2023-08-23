from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

class Category(models.Model) :
    name = models.CharField(max_length=255)  

    def __str__(self):
        return self.name
    


    
class post(models.Model):
    image = models.ImageField(upload_to='blog',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    count_views = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    login_requier = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    
    def __str__(self):
        return "{}-{}".format(self.title,self.id)


class Comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Meta:
    ordering = ['created_date']
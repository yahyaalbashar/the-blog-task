from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    publish_date= models.DateTimeField(auto_now=False,auto_now_add=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')
    category=models.ManyToManyField('Category')

    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.title

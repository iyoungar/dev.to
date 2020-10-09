from django.db import models

# Create your models here.
class UserPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    tags = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
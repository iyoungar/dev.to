from django.db import models

# Create your models here.
class UserPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title




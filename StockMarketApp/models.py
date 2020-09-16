from django.db import models

# Create your models here.
class userinfo(models.Model):
    Name = models.CharField(max_length= 264)
    Email = models.CharField(max_length = 264)
    Text = models.TextField(max_length = 1000, unique = True)

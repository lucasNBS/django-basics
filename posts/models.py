from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=50, blank=False, null=False, unique=True)
  description = models.CharField(max_length=50, blank=False, null=False)
  image = models.ImageField(upload_to='images', default="images/no-image.jpg")
  content = models.TextField(blank=False, null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
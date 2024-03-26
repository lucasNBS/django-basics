from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=50, blank=False, null=False, unique=True)
  description = models.CharField(max_length=50, blank=False, null=False)
  content = models.TextField(blank=False, null=False)
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=6)
    created = models.DateField(auto_now_add=True)
    content = models.TextField()


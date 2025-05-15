from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=200)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        ordering = ['-created_datetime']

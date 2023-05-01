from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    author = models.ForeignKey(User, null= True, on_delete=models.SET_NULL,verbose_name='author')

    def __str__(self):
        return self.title
   
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, null= True, on_delete=models.SET_NULL, verbose_name='author')

    def __str__(self):
        return self.content

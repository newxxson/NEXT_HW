from django.db import models
from Accounts.models import Account

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='my_posts', null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, verbose_name='author')
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment
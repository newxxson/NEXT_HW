from django.db import models

# Create your models here.
class Article(models.Model):
    
    category = [
        ('N/A', 'N/A'),
        ('HOBBY', 'Hobby'),
        ('FOOD', 'Food'),
        ('PROGRAMMING', 'Programming'),
    ]
    article_category = models.CharField(max_length=20, choices=category, default='N/A')
    title = models.CharField(max_length=200)
    content = models.TextField()
    written_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title



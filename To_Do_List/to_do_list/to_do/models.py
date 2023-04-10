from django.db import models

# Create your models here.
class To_Do_Element(models.Model):
    title = models.TextField()
    content = models.TextField()
    due_date = models.DateTimeField()
    done = models.BooleanField()

    def __str__(self) -> str:
        return self.title
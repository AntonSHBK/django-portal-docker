from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    
    
    def __str__(self):
        return self.question_text    
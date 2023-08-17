from ckeditor.fields import RichTextField

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'
        
    title = models.CharField(max_length=200, db_index=True)
    # content = models.TextField(max_length=5000, blank=True, null=True)
    content = RichTextField(max_length=5000, blank=True, null=True, config_name='admin_post')
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True, null=True)  
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True)
    reply = models.ForeignKey('self', null=True, blank=True, related_name='reply_ok', on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.title     
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def total_lkes(self):        
        return self.likes.count()
    
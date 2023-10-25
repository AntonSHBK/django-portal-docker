from ckeditor.fields import RichTextField

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    '''
    About this class...
    '''    
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        
    title = models.CharField(
        max_length=200,
        help_text='Не более 200 символов',
        db_index=True,
        verbose_name=_("Title")
        )
    
    content = RichTextField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name=_("Content")
        )
    
    date_created = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Date of create")
        )
    
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date of update")
        )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Author")
        )
    
    slug = models.SlugField(
        max_length=50,
        unique=True, 
        null=True,
        verbose_name=_("Slug")
        )
      
    likes = models.ManyToManyField(
        User, 
        related_name='postcomment', 
        blank=True, 
        verbose_name=_("Likes")
    )
    
    reply = models.ForeignKey('self',
                              null=True, 
                              related_name='reply_ok',
                              on_delete=models.CASCADE,
                              verbose_name=_("Reply")
                              ) 
    
    saves_posts = models.ManyToManyField(
        User,
        related_name='blog_posts_save',
        blank=True,
        verbose_name=_("Saved user's posts")
    )
     
    def __str__(self):
        return self.title     
    
    def get_absolute_url(self):
        return reverse(viewname='blog:user-post-list', kwargs={'username': self.author})
    
    def get_total_likes(self):        
        return self.likes.count()
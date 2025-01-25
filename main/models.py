from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name')
    agrees = models.ManyToManyField(User, related_name='post_agrees', blank=True)
    disagrees = models.ManyToManyField(User, related_name='post_disagrees', blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title} • {self.author}'
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def total_agrees(self):
        return self.agrees.count()

    def total_disagrees(self):
        return self.disagrees.count()
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} • {self.post}'
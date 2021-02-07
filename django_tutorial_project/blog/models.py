from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #a few options: auto_now is better to use for when post are edited or updated; auto_now_add is too static, cannot change later
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
    return self.title

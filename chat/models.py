from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class user_bot(models.Model):
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

class Message(models.Model):
    author = models.ForeignKey(user_bot,related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()

    def __str__(self):
        return self.content

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:1]





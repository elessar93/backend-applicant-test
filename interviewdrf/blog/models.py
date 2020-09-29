from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    published_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    content = models.CharField(max_length=512)
    related_tags = models.CharField(max_length=256)
    related_user = models.ForeignKey(User, models.DO_NOTHING)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=128)
    comment = models.CharField(max_length=128)
    send_date = models.DateTimeField(auto_now_add=True)
    related_user = models.ForeignKey(User, models.DO_NOTHING)
    related_blog = models.ForeignKey(Blog, models.CASCADE)

    def __str__(self):
        return self.title

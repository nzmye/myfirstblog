from django.db import models
from django.utils import  timezone
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User')
    head=models.CharField(max_length=200)
    text=models.TextField()
    creating_date=models.DateTimeField(timezone.now(), null=True)
    publish_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
         return self.head


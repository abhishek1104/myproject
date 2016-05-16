from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime 
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text =  models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
        default = timezone.now)
    publish_date = models.DateTimeField(
        blank=False,null=False)



    def publish(self): #def means that this is a function/method and publish is the name of the method.
        self.publish_date = timezone.now()
        self.save()


    def __str__ (self):
        return self.title





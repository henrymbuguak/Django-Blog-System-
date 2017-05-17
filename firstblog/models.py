from __future__ import unicode_literals

from django.db import models

class posts(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    bodyText = models.TextField()
    timeStamp = models.DateField()

from __future__ import unicode_literals
from django.db import models


class SpiderContent(models.Model):

    name = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now_add=True)
    category = models.TextField(blank=False, default='n/a')
    content = models.TextField(blank=True, default='')
    content_length = models.TextField(blank=True, default='')

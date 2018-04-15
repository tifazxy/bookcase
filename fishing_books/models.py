# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Storage(models.Model):
    """Storge all books"""
    book_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
            
    def __unicode__(self):
        """return string Display"""
        return self.book_name
        
class Comment(models.Model):
    """owner of books"""
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    commentor_name = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """return string Display"""
        return self.text[:25] + "..."

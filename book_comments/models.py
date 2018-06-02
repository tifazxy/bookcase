# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ArticleInformation(models.Model):
    """article information"""
    article_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class ArticleScore(models.Model):
    """article score"""
    article = models.ForeignKey(ArticleInformation, on_delete=models.CASCADE)
    score = models.FloatField()


class ArticleVotes(models.Model):
    """article votes"""
    votes = models.IntegerField()
    article = models.ForeignKey(ArticleInformation, on_delete=models.CASCADE)


class Voters(models.Model):
    """voters"""
    article = models.ForeignKey(ArticleInformation, on_delete=models.CASCADE)
    voter_id = models.CharField(max_length=200)

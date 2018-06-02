# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import redis
import time
import json

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import ArticleInformation
from .forms import ArticleForm


# Create your views here.
# ONE_WEEK_IN_SECONDS = 7 * 86400
# VOTE_SCORE = 432
# r_pool = redis.ConnectionPool()
# r = redis.StrictRedis(connection_pool=r_pool)
# ARTICLES_PER_PAGE = 25


def comments(request):
    # context = {'articles': get_article(r, 1, order='score:')}
    articles = ArticleInformation.objects.order_by('date')
    context = {'articles': articles}
    return render(request, 'book_comments/comments.html', context)


def add_comments(request):
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            add_comments = form.save(commit=False)
            add_comments.owner = request.user
            add_comments.save()
            # post_article(r, request.user, form.title, form.link)
            return HttpResponseRedirect(reverse('book_comments:comments'))
    context = {'form': form}
    return render(request, 'book_comments/add_comments.html', context)


def article_detail(request, article_id):
    # context = {'articles': get_article(r, 1, order='score:')}
    article = ArticleInformation.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'book_comments/article.html', context)


# def article_vote(conn, user, article):
#     cutoff = time.time() - ONE_WEEK_IN_SECONDS
#     if conn.zscore('time:', article) < cutoff:
#         return
#
#     article_id = article.partition(':')[-1]
#     if conn.sadd('voted:' + article_id, user):
#         conn.zincrby('score:', article, VOTE_SCORE)
#         conn.hincrby(article, 'votes', 1)
#
#
# def post_article(conn, user, title, link):
#     article_id = str(conn.incr('article:'))
#
#     voted = 'voted：' + article_id
#     conn.sadd(voted, user)
#     conn.expire(voted, ONE_WEEK_IN_SECONDS)
#
#     now = time.time()
#     article = 'article:' + article_id
#     conn.hmset(article, {
#         'title': title,
#         'link': link,
#         'poster': user,
#         'time': now,
#         'votes': 1,
#     })
#     conn.zadd('score:', article, now + VOTE_SCORE)
#     conn.zadd('TIME:', article, now)
#
#     return article_id
#
#
# def get_article(conn, page, order='score:'):
#     start = (page-1) * ARTICLES_PER_PAGE
#     end = start + ARTICLES_PER_PAGE
#
#     ids = conn.zrevrange(order, start, end)
#     articles = []
#     for id in ids:
#         article_data = conn.hgetall(id)
#         article_data['id'] = id
#         articles.append(article_data)
#
#     return articles


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Storage, Comment

# Create your views here.
def index(request):
    """index page"""
    #render(request, templete)
    return render(request, 'fishing_books/index.html')
    
def All_storage(request):
    """All the book storage"""
    storages = Storage.objects.order_by('date_added')
    
    context = {'storages' : storages}
    return render(request, 'fishing_books/storage.html', context)
    
def storage_all_comment(request, book_id):
    """All comments for books"""
    storage = Storage.objects.get(id = book_id)
    comments = storage.comment_set.order_by('date_added')
    
    context = {'storage' : storage, 'comments' : comments}
    return render(request, 'fishing_books/comment.html', context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Storage, Comment
from .forms import StorageForm, CommentForm

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

def new_storage(request): 
    """add a new book"""
    if request.method != 'POST':
        form = StorageForm()
    else:
        form = StorageForm(request.POST)
        if form.is_valid():
            new_storage = form.save(commit=False)
            #new_topic.owner = request.user
            new_storage.save()
            return HttpResponseRedirect(reverse('fishing_books:storage'))
    context = {'form' : form}
    return render(request, 'fishing_books/new_storage.html', context)
    
#~ def new_comment(request, book_id): 
    #~ """add a new comment"""
    #~ storage = Storage.objects.get(id=book_id)
    #~ if request.method != 'POST':
        #~ form = CommentForm()
    #~ else:
        #~ form = CommentForm(data=request.POST)
        #~ if form.is_valid():
            #~ new_comment = form.save(commit=False)
            #~ new_comment.storage = storage
            #~ #new_topic.owner = request.user
            #~ new_comment.save()
            #~ return HttpResponseRedirect(reverse('fishing_books:comment',
            #~ args=[book_id]))
    #~ context = {'form' : form, 'storage' : storage}
    #~ return render(request, 'fishing_books/new_comment.html', context)
    









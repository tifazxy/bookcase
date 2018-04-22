# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from .models import Storage, Comment
from .forms import StorageForm, CommentForm

# Create your views here.
def index(request):
    """index page"""
    #render(request, templete)
    return render(request, 'fishing_books/index.html')

@login_required    
def All_storage(request):
    """All the book storage"""
    storages = Storage.objects.filter(owner=request.user).order_by('date_added')
    context = {'storages' : storages}
    return render(request, 'fishing_books/storage.html', context)

@login_required    
def storage_all_comment(request, book_id):
    """All comments for books"""
    storage = Storage.objects.get(id = book_id)
    check_storage_owner(storage, request)
    comments = storage.comment_set.order_by('date_added')
    context = {'storage' : storage, 'comments' : comments}
    return render(request, 'fishing_books/comment.html', context)

@login_required
def new_storage(request): 
    """add a new book"""
    if request.method != 'POST':
        form = StorageForm()
    else:
        form = StorageForm(request.POST)
        if form.is_valid():
            new_storage = form.save(commit=False)
            new_storage.owner = request.user
            new_storage.save()
            return HttpResponseRedirect(reverse('fishing_books:storage'))
    context = {'form' : form}
    return render(request, 'fishing_books/new_storage.html', context)

@login_required    
def new_comment(request, book_id):
    """add a new comment"""
    storage = Storage.objects.get(id=book_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.storage = storage
            new_comment.save()
            return HttpResponseRedirect(reverse('fishing_books:comment',
            args=[book_id]))
    context = {'form' : form, 'storage' : storage}
    return render(request, 'fishing_books/new_comment.html', context)
    
@login_required        
def edit_comment(request, comment_id):
    """edit exist comment""" 
    comment = Comment.objects.get(id=comment_id)
    storage = comment.storage
    check_storage_owner(storage, request)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fishing_books:comment',
            args=[storage.id]))
    context = {'comment': comment, 'storage': storage, 'form': form}
    return render(request, 'fishing_books/edit_comment.html', context)
    
def check_storage_owner(storage, request):
    if storage.owner != request.user:
        raise Http404








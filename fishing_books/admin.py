# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from fishing_books.models import Storage, Comment

# Register your models here.
admin.site.register(Storage)
admin.site.register(Comment)

"""define url pattens"""

from django.conf.urls import url

# import from current folder
from . import views

urlpatterns = [
    # ''means start and end position; ^ means begining, $ means ending; '^$' 
    # means an url which begining and ending with nothing  
    url(r'^$', views.index, name='index'),
    
    url(r'^storage/$', views.All_storage, name='storage'),
    
    url(r'^new_storage/$', views.new_storage, name='new_storage'),
    
    url(r'^storage/(?P<book_id>\d+)/$', 
    views.storage_all_comment, name='comment'),
    
    url(r'^new_comment/(?P<book_id>\d+)/$', 
    views.new_comment, name='new_comment'),
    
    url(r'^edit_comment/(?P<comment_id>\d+)/$', 
    views.edit_comment, name='edit_comment'),

]

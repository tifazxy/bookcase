"""define url pattens"""

from django.conf.urls import url

# import from current folder
from . import views

urlpatterns = [
    # ''means start and end position; ^ means begining, $ means ending; '^$' 
    # means an url which begining and ending with nothing  
    url(r'^$', views.index, name='index'),
    
    url(r'^storage/$', views.All_storage, name='storage'),
    
    url(r'^storage/(?P<book_id>\d+)/$', views.storage_all_comment, name='comment'),

]

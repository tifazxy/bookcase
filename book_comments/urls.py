"""define url pattens"""

from django.conf.urls import url

# import from current folder
from . import views

urlpatterns = [
    # ''means start and end position; ^ means begining, $ means ending; '^$' 
    # means an url which begining and ending with nothing
    url(r'^article/$', views.comments, name='comments'),

    url(r'^add_comments/$', views.add_comments, name='add_comments'),

    url(r'^detail/(?P<article_id>\d+)/$', views.article_detail, name='article_detail'),

]

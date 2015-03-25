from django.conf.urls import *
urlpatterns=patterns(('sblog.views'),url(r'^bloglist/$','blog_list',name='bloglist'),
url(r'^blog/(?P<id>\d+)/$','blog_show',name='detailblog')
)
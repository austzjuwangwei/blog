from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sblog/',include('sblog.urls')),
)
urlpatterns += patterns((''),(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'D:/Python27/blog/static'}),)

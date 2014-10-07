__author__ = 'mj'
from django.conf.urls import patterns, url

urlpatterns = patterns('snippet.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)


__author__ = 'mj'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippet.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
# This will enable working of the suffix like .json and .yaml etc
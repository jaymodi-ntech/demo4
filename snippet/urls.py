__author__ = 'mj'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views
# version 1. This was supported for function views
# urlpatterns = patterns('snippet.views',
#     url(r'^snippets/$', 'snippet_list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
# )

# This new urlpatterns are supporting class based views
urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^blogs/$', views.BlogList.as_view()),
    url(r'^blogs/(?P<pk>[0-9]+)/$', views.BlogDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
# This will enable working of the suffix like .json and .yaml etc
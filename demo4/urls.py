from django.conf.urls import patterns, include, url
from snippet import urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('snippet.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

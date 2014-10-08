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
    url(r'^mj_auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
#     I can use whatever i want to use at the mj_auth place.
#     just make sure that the name_space is as it is.
#     Rest is fine.
)

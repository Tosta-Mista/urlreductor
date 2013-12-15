from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mini_url.views.list'),
    url(r'^urlfactory/', include('mini_url.urls')),
    # Examples:
    # url(r'^$', 'urlreductor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

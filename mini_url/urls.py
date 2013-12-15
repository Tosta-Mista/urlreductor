# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('mini_url.views',
        url(r'^$', 'list', name='url_list'),
        url(r'^new/$', 'new', name='new_url'),
        url(r'^(?P<secret>\w{10})/$', 'redirection', name='url_redirection'),
)
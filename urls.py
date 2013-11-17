from django.conf.urls.defaults import *
import os

urlpatterns = patterns('dj_dh',
    (r'^$', 'views.index'),
    (r'^finish_dh/$', 'views.finish'),
)

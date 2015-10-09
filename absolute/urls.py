from django import get_version
from distutils.version import StrictVersion
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
if StrictVersion(get_version()) > StrictVersion('1.7.0'):
    urlpatterns = []
else:
    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'absolute.views.home', name='home'),
        # url(r'^absolute/', include('absolute.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        # url(r'^admin/', include(admin.site.urls)),
    )

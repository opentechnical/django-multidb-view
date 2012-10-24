from django.conf.urls import patterns, include, url
from dbview.api import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
test1_resource = Test1Resource()
test2_resource = Test2Resource()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'multidb.views.home', name='home'),
    # url(r'^multidb/', include('multidb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(test1_resource.urls)),
    url(r'^api/', include(test2_resource.urls)),    
)

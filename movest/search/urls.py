from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:                                                                                                                                            
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('search.views',
    # search                                                                                                                                                                                 
    url(r'^$', 'index'),
)

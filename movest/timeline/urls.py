from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('timeline.views',
    # timeline
    url(r'^$', 'index'),
    url(r'^timeline/', 'timeline'),
    url(r'^data.json', 'get_data'),   
)

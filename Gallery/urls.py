from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^albums/',include('albums.urls')),
    url(r'^auth/',include('loginsys.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':'D:/Django_code/Gallery/Gallery/media'}),
    url(r'^admin_tools/', include('admin_tools.urls')),
)
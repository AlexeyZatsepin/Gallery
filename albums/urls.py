from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
  url(r'^all/$', views.albums),
  url(r"^get/(?P<id>\d+)/$", views.album),
  url(r"^add_like/(?P<id>\d+)/$", views.add_like),
  url(r"^photo/get/(?P<id>\d+)/$", views.photo),
  url(r"^add_comment/(?P<id>\d+)/$", views.add_comment),
  url(r"^add_like_photo/(?P<id>\d+)/$", views.add_like_photo),
  url(r"^page/(\d+)/$",views.albums),
  url(r'^search/$', views.search),
  url(r'^add_album/$',views.add_album),
  url(r'^add_album1/$',views.add_album1),
  url(r'^my_albums/$',views.my_albums),
  url(r"^add_photo/(?P<id>\d+)/$", views.add_photo),
  url(r"^add_like_comment/(?P<id>\d+)/(?P<photo_id>\d+)/$", views.add_like_comment),
  #url(r'^my_comments/$',views.my_comments)
)
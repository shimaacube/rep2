from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
from blog.models import Post
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail), #for post/1/
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^welcome/', views.welcome),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # url(r"^delete_comment/(\d+)/$", "delete_comment"),
	# url(r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
	


   
    
)  